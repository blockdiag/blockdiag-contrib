# -*- coding: utf-8 -*-
#  Copyright 2012 Takeshi KOMIYA
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

import re
from blockdiag.imagedraw import simplesvg
from blockdiag.imagedraw.svg import SVGImageDraw

class animate(simplesvg.base):
    def __init__(self, *args, **kwargs):
        super(animate, self).__init__(*args, **kwargs)

        self.add_attribute('attributeType', 'XML')
        self.add_attribute('attributeName', 'opacity')

    def set_animation(self, dur=None, _from=None, _to=None):
        if dur:
           self.add_attribute('dur', dur)

        if _from:
           self.add_attribute('from', _from)

        if _to:
           self.add_attribute('to', _to)


class AnimatedSVGImageDraw(SVGImageDraw):
    def save(self, filename, size, _format):
        if filename:
            self.filename = filename

        if size:
            self.svg.attributes['width'] = size[0]
            self.svg.attributes['height'] = size[1]

        self.set_animation()
        image = self.svg.to_xml()

        if self.filename:
            open(self.filename, 'w').write(image)

        return image

    def set_animation(self):
        for i, elem in enumerate(self.svg.elements[3:]):
            anim = animate(id='anim%d' % i)
            anim.set_animation('1s', '0', '1')
            anim.add_attribute('fill', 'freeze')

            if i == 0:
                anim.add_attribute('begin', '0s')
            else:
                anim.add_attribute('begin', 'anim%d.end' % (i - 1))

            style = elem.attributes.get('style', '')
            if re.match('filter:', style):
                elem.attributes['style'] = re.sub(';opacity:0.7', '', style)
                elem.attributes['to'] = '0.7'

            elem.attributes['opacity'] = '0'
            elem.elements.append(anim)


def setup(self):
    from blockdiag.imagedraw import install_imagedrawer
    install_imagedrawer('animated.svg', AnimatedSVGImageDraw)
