# -*- coding: utf-8 -*-
#  Copyright 2011 Takeshi KOMIYA
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
import os
from blockdiag.noderenderer import NodeShape
from blockdiag.noderenderer import install_renderer
from blockdiag.utils.XY import XY

try:
    from blockdiag.utils.PILTextFolder import PILTextFolder as TextFolder
except ImportError:
    from blockdiag.utils.TextFolder import TextFolder


def gen_image_class(image_path):
    class CiscoImage(NodeShape):
        def __init__(self, node, metrix=None):
            super(CiscoImage, self).__init__(node, metrix)

            self.textalign = 'left'
            self.image_path = image_path

            size = self.image_size

            pt = metrix.cell(node).center()
            self.image_box = [pt.x - size[0] / 2, pt.y - size[1] / 2,
                              pt.x + size[0] / 2, pt.y + size[1] / 2]

            width = metrix.nodeWidth / 2 - size[0] / 2 + metrix.cellSize
            self.textbox = [pt.x + size[0] / 2, pt.y - size[1] / 2,
                            pt.x + size[0] / 2 + width, pt.y + size[1] / 2]

            folder = TextFolder(self.textbox, node.label,
                                halign=self.textalign,
                                font=self.metrix.font,
                                fontsize=self.metrix.fontSize)
            textbox = folder.outlineBox()

            self.connectors[0] = XY(pt.x, self.image_box[1])
            self.connectors[1] = XY(textbox[2] + self.metrix.nodePadding, pt.y)
            self.connectors[2] = XY(pt.x, self.image_box[3])
            self.connectors[3] = XY(self.image_box[0], pt.y)

        @property
        def image_size(self):
            import PIL.Image

            size = PIL.Image.open(image_path).size
            box = [self.metrix.nodeWidth, self.metrix.nodeHeight]

            if box[0] < size[0] or box[1] < size[1]:
                if (size[0] * 1.0 / box[0]) < (size[1] * 1.0 / box[1]):
                    size = (size[0] * box[1] / size[1], box[1])
                else:
                    size = (box[0], size[1] * box[0] / size[0])

            return size

        def render_shape(self, drawer, format, **kwargs):
            if not kwargs.get('shadow'):
                drawer.loadImage(self.image_path, self.image_box)

    return CiscoImage

def to_classname(filename):
    filename = re.sub('\.[a-z]+$', '', filename)
    filename = re.sub(' ', '_', filename)

    return "cisco.%s" % filename

def setup(self):
    path = "%s/images/cisco" % os.path.dirname(__file__)
    dir = os.listdir(path)
    for filename in dir:
        klass = gen_image_class("%s/%s" % (path, filename))
        klassname = to_classname(filename)

        install_renderer(klassname, klass)
