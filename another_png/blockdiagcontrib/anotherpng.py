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

import Image
import ImageDraw
from blockdiag.imagedraw import base
from blockdiag.imagedraw.png import dashize_line


class PNGImageDraw(base.ImageDraw):
    def __init__(self, filename, **kwargs):
        self.filename = filename
        self.image = None
        self.drawer = None

    def set_canvas_size(self, size):
        self.image = Image.new('RGBA', size)
        self.drawer = ImageDraw.Draw(self.image)

    def rectangle(self, box, **kwargs):
        fill = kwargs.get('fill')
        if fill:
            for x in range(box.x1, box.x2 + 1):
                for y in range(box.y1, box.y2 + 1):
                    self.drawer.point((x, y), fill=fill)

        outline = kwargs.get('outline')
        if outline:
            for x in range(box.x1, box.x2 + 1):
                self.drawer.point((x, box.y1), fill=outline)
                self.drawer.point((x, box.y2), fill=outline)

            for y in range(box.y1, box.y2 + 1):
                self.drawer.point((box.x1, y), fill=outline)
                self.drawer.point((box.x2, y), fill=outline)

    def save(self, filename, size, format):
        self.image.save(self.filename, 'PNG')


def setup(self):
    from blockdiag.imagedraw import install_imagedrawer
    install_imagedrawer('another.png', PNGImageDraw)
