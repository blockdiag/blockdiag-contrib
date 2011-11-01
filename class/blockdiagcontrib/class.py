# -*- coding: utf-8 -*-
from blockdiag.noderenderer.box import Box
from blockdiag.noderenderer import install_renderer
from blockdiag.utils import XY


class Class(Box):
    def render_shape(self, drawer, format, **kwargs):
        super(Class, self).render_shape(drawer, format, **kwargs)

        fill = kwargs.get('fill')

        r = self.metrics.node_height / 3

        if not kwargs.get('shadow'):
            box = self.textbox

            line = (XY(box[0], box[1] + r), XY(box[2], box[1] + r))
            drawer.line(line, fill=fill)

            line = (XY(box[0], box[1] + r + 4), XY(box[2], box[1] + r + 4))
            drawer.line(line, fill=fill)

    def render_label(self, drawer, **kwargs):
        fill = kwargs.get('fill')

        r = self.metrics.node_height / 3

        if not kwargs.get('shadow'):
            box = self.textbox

            texts = self.node.label.split('|')

            classbox = (box[0], box[1], box[2], box[1] + r)
            drawer.textarea(classbox, texts[0],
                            fill=fill, halign=self.textalign,
                            fontsize=self.node.fontsize,
                            lineSpacing=self.metrics.line_spacing)

            variablebox = (box[0], box[1] + r + 4, box[2], box[3])
            drawer.textarea(variablebox, texts[1],
                            fill=fill, halign='left', valign='top',
                            fontsize=self.node.fontsize,
                            lineSpacing=self.metrics.line_spacing)


def setup(self):
    install_renderer('class', Class)
