# -*- coding: utf-8 -*-
#  Copyright 2014 Takeshi KOMIYA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import io
import re
from PIL import Image
from functools import wraps
from blockdiag.imagedraw import base
from blockdiag.imagedraw.utils import cached
from blockdiag.utils import images, XY, Box, Size, is_Pillow_available
from blockdiag.utils.compat import u


def get_eps_fontname(font):
    if font.name:
        fontname = font.name
    else:
        if font.generic_family == 'serif':
            fontname = 'Times'
        elif font.generic_family == 'sansserif':
            fontname = 'Helvetica'
        elif font.generic_family == 'monospace':
            fontname = 'Courier'
        else:
            msg = "Unsupported font: %s" % font.generic_family
            raise NotImplemented(msg)

        if font.weight == 'bold':
            fontname += '-Bold'
        elif font.style in ('italic', 'oblique'):
            if fontname == 'Times':
                fontname += '-Italic'
            else:
                fontname += '-Oblique'
        else:  # normal style
            if fontname == 'Times':
                fontname += '-Roman'

    return fontname


def graphic_state(fn):
    @wraps(fn)
    def func(self, *args, **kwargs):
        self.buffer.append(u("gsave\n"))
        ret = fn(self, *args, **kwargs)
        self.buffer.append(u("grestore\n"))
        return ret

    return func


class EPSImageDraw(base.ImageDraw):
    baseline_text_rendering = True

    def __init__(self, filename, **kwargs):
        self.filename = filename
        self.size = Size(0, 0)
        self.buffer = []

    def write(self, msg, *args):
        self.buffer.append(u(msg + "\n") % args)

    def remap(self, obj):
        if isinstance(obj, (XY, tuple)) and len(obj) == 2:
            return XY(obj[0], self.size.y - obj[1])
        elif isinstance(obj, (Box, tuple)) and len(obj) == 4:
            return Box(obj[0], self.size.y - obj[3],
                       obj[2], self.size.y - obj[1])
        else:
            return obj

    def set_canvas_size(self, size):
        self.size = size

    def set_rgbcolor(self, color):
        rgb = tuple(c % 256.0 for c in color)
        self.write("%f %f %f setrgbcolor", *rgb)

    def set_style(self, style, thick):
        if thick is None:
            thick = 1

        if style == 'dotted':
            self.write("[%d %d] 0 setdash", 2 * thick, 2 * thick)
        elif style == 'dashed':
            self.write("[%d %d] 0 setdash", 4 * thick, 4 * thick)
        elif style == 'none':
            self.buffer.append(u("[0 65535] 0 setdash\n"))
        elif re.search('^\d+(,\d+)*$', style or ""):
            pattern = [int(n) * thick for n in style.split(',')]
            self.write("[%s] 0 setdash", " ".join(pattern))

    def set_linewidth(self, thick):
        if thick:
            self.write("%d setlinewidth", thick)

    def render_path(self, **kwargs):
        fill = kwargs.get('fill', 'none')
        if fill != 'none':
            self.write('gsave')
            self.set_rgbcolor(fill)
            self.write('fill')
            self.write('grestore')

        outline = kwargs.get('outline', fill)
        self.set_rgbcolor(outline)
        self.write('stroke')

    @graphic_state
    def line(self, xy, **kwargs):
        fill = kwargs.get('fill', 'none')
        if fill == 'none':
            return

        self.set_rgbcolor(fill)
        self.set_style(kwargs.get('style'), kwargs.get('thick'))
        self.set_linewidth(kwargs.get('thick'))

        self.write('newpath')
        self.write('%d %d moveto', *self.remap(xy[0]))
        for pt in xy[1:]:
            self.write('%d %d lineto', *self.remap(pt))
        self.write('closepath stroke')

    @graphic_state
    def rectangle(self, box, **kwargs):
        self.set_style(kwargs.get('style'), kwargs.get('thick'))
        self.set_linewidth(kwargs.get('thick'))

        box = self.remap(box)
        self.write("newpath")
        self.write("%d %d moveto", *box.topleft)
        self.write("%d %d lineto", *box.topright)
        self.write("%d %d lineto", *box.bottomright)
        self.write("%d %d lineto", *box.bottomleft)
        self.write("closepath")

        self.render_path(**kwargs)

    @graphic_state
    def polygon(self, xy, **kwargs):
        self.set_style(kwargs.get('style'), kwargs.get('thick'))

        self.write("newpath")
        self.write("%d %d moveto", *self.remap(xy[0]))
        for pt in xy[1:]:
            self.write("%d %d lineto", *self.remap(pt))
        self.write("closepath")

        self.render_path(**kwargs)

    @graphic_state
    def arc(self, box, start, end, **kwargs):
        fill = kwargs.get('fill', 'none')
        if fill == 'none':
            return

        box = self.remap(box)
        start, end = 360 - end, 360 - start
        w = box.width / 2
        h = box.height / 2

        self.set_rgbcolor(fill)
        self.set_style(kwargs.get('style'), kwargs.get('thick'))
        self.write("/savematrix matrix currentmatrix def")
        self.write("%d %d translate", *box.center)
        self.write("%d %d scale", w, h)
        self.write("newpath")
        self.write("0 0 1 %d %d arc", start, end)
        self.write("savematrix setmatrix")
        self.write("stroke")

    @graphic_state
    def ellipse(self, box, **kwargs):
        box = self.remap(box)
        w = box.width / 2
        h = box.height / 2

        self.set_style(kwargs.get('style'), kwargs.get('thick'))
        self.write("/savematrix matrix currentmatrix def")
        self.write("%d %d translate", *box.center)
        self.write("%d %d scale", w, h)
        self.write("newpath")
        self.write("0 0 1 0 360 arc")
        self.write("savematrix setmatrix")

        self.render_path(**kwargs)

    @cached
    def textlinesize(self, string, font, **kwargs):
        if is_Pillow_available():
            if not hasattr(self, '_pil_drawer'):
                from blockdiag.imagedraw import png
                self._pil_drawer = png.ImageDrawEx(None)

            return self._pil_drawer.textlinesize(string, font)
        else:
            from blockdiag.imagedraw.utils import textsize
            return textsize(string, font)

    def set_font(self, font):
        self.write("/%s findfont", get_eps_fontname(font))
        self.write("%d scalefont", font.size)
        self.write("setfont")

    def text(self, xy, string, font, **kwargs):
        self.set_font(font)
        self.write("%d %d moveto", *self.remap(xy))
        self.write("(%s) show", string)

    @graphic_state
    def textarea(self, box, string, font, **kwargs):
        if 'rotate' in kwargs and kwargs['rotate'] != 0:
            angle = 360 - int(kwargs['rotate']) % 360
            self.write("%d rotate", angle)

            if angle == 90:
                box = Box(-box.y2, box.x1, -box.y1, box.x1 + box.width)
                box = box.shift(x=self.size.y, y=self.size.y)
            elif angle == 180:
                box = Box(-box.x2, -box.y2, -box.x1, -box.y2 + box.height)
                box = box.shift(y=self.size.y * 2)
            elif angle == 270:
                box = Box(box.y1, -box.x2, box.y2, -box.x1)
                box = box.shift(x=-self.size.y, y=self.size.y)

        lines = self.textfolder(box, string, font, **kwargs)

        if kwargs.get('outline'):
            outline = kwargs.get('outline')
            self.rectangle(lines.outlinebox, fill='white', outline=outline)

        rendered = False
        for string, xy in lines.lines:
            self.text(xy, string, font, **kwargs)
            rendered = True

        if not rendered and font.size > 0:
            font.size = int(font.size * 0.8)
            self.textarea(box, string, font, **kwargs)

    @graphic_state
    def image(self, box, url):
        box = self.remap(box)
        try:
            stream = images.open(url)
            image = Image.open(stream)

            # resize image.
            w = min([box.width, image.size[0]])
            h = min([box.height, image.size[1]])
            image.thumbnail((w, h), Image.ANTIALIAS)
            image = image.convert('RGB')

            # centering image.
            w, h = image.size
            if box.width > w:
                x = box[0] + (box.width - w) // 2
            else:
                x = box[0]

            if box.height > h:
                y = box[1] + (box.height - h) // 2
            else:
                y = box[1]

            size = w * h * 3  # size of bitmap (24bit color)
            self.write("%d %d translate", x, y + h)
            self.write("/imgdata %d string def", size)
            self.write("%d %d 8 [1 0 0 -1 0 1]", w, h)
            self.write("{ currentfile imgdata readhexstring pop }")
            self.write("false 3 colorimage")
            for i, rgb in enumerate(image.getdata()):
                self.write("%x%x%x", *rgb)
        except IOError:
            stream = None
        finally:
            if stream:
                stream.close()

    def save(self, filename, size, _format):
        if filename:
            self.filename = filename

        with io.open(self.filename, 'w', encoding='utf-8') as fd:
            fd.write(u("%!PS-Adobe-3.0 EPSF-3.0\n"))
            fd.write(u("%%%%BoundingBox: 0 0 %d %d\n") % self.size)
            fd.write(u("%%%%HiResBoundingBox: 0 0 %f %f\n") % self.size)
            for line in self.buffer:
                fd.write(line)


def setup(self):
    from blockdiag.imagedraw import install_imagedrawer
    install_imagedrawer('eps', EPSImageDraw)
