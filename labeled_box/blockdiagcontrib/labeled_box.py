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

from blockdiag.noderenderer import NodeShape
from blockdiag.noderenderer import install_renderer
from blockdiag.noderenderer.box import Box as BoxShape
from blockdiag.plugins import NodeHandler
from blockdiag.plugins import install_node_handler
from blockdiag.utils import Box


class LabeledBox(BoxShape):
    def __init__(self, node, metrics=None):
        super(LabeledBox, self).__init__(node, metrics)

    @property
    def labelbox(self):
        if self.node.toplabel:
            font = self.metrics.font_for(self.node)
            textsize = self.metrics.textsize(self.node.toplabel, font=font)

            box = self.metrics.cell(self.node).box
            box[3] = box.y1 + textsize.y
        else:
            box = Box(0, 0, 0, 0)

        return box

    def get_textbox(self):
        if self.node.toplabel:
            font = self.metrics.font_for(self.node)
            textsize = self.metrics.textsize(self.node.toplabel, font=font)

            box = self.metrics.cell(self.node).box
            box[1] += textsize.y + self.metrics.cellsize
        else:
            box = self.metrics.cell(self.node).box

        return box

    def render_shape(self, drawer, format, **kwargs):
        fill = kwargs.get('fill')

        # recalcurate bounds of textbox
        self.textbox = self.get_textbox()

        # draw outline
        box = self.get_textbox()

        if kwargs.get('shadow'):
            box = self.shift_shadow(box)
            if kwargs.get('style') == 'blur':
                drawer.rectangle(box, fill=fill, outline=fill,
                                 filter='transp-blur')
            else:
                drawer.rectangle(box, fill=fill, outline=fill)
        elif self.node.background:
            drawer.rectangle(box, fill=self.node.color,
                             outline=self.node.color)
            drawer.loadImage(self.node.background, self.textbox)
            drawer.rectangle(box, outline=self.node.linecolor,
                             style=self.node.style)
        else:
            drawer.rectangle(box, fill=self.node.color,
                             outline=self.node.linecolor,
                             style=self.node.style)

    def render_label(self, drawer, **kwargs):
        super(LabeledBox, self).render_label(drawer, **kwargs)

        if not kwargs.get('shadow') and self.node.toplabel:
            font = self.metrics.font_for(self.node)
            drawer.textarea(self.labelbox, self.node.toplabel, font,
                            fill=self.node.textcolor, halign=self.textalign,
                            line_spacing=self.metrics.line_spacing)


class LabeledBoxHandler(NodeHandler):
    def on_attr_changed(self, node, attr):
        if attr.name == 'shape' and attr.value == 'labeled_box':
            node.toplabel = None


def setup(self):
    install_renderer('labeled_box', LabeledBox)
    install_node_handler(LabeledBoxHandler(None))
