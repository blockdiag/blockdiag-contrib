# -*- coding: utf-8 -*-
from blockdiag.noderenderer.box import Box
from blockdiag.noderenderer import install_renderer
from blockdiag.utils.XY import XY


class Class(Box):
    def render_shape(self, drawer, format, **kwargs):
        super(Class, self).render_shape(drawer, format, **kwargs)

        fill = kwargs.get('fill')

        r = self.metrix.nodeHeight / 3

        if not kwargs.get('shadow'):
            box = self.textbox

            line = (XY(box[0], box[1] + r), XY(box[2], box[1] + r))
            drawer.line(line, fill=fill)

            line = (XY(box[0], box[1] + r + 4), XY(box[2], box[1] + r + 4))
            drawer.line(line, fill=fill)

    def render_label(self, drawer, **kwargs):
        font = kwargs.get('font')
        fill = kwargs.get('fill')

        r = self.metrix.nodeHeight / 3

        if not kwargs.get('shadow'):
            box = self.textbox

            texts = self.node.label.split('|')

            classbox = (box[0], box[1], box[2], box[1] + r)
            drawer.textarea(classbox, texts[0],
                            fill=fill, halign=self.textalign,
                            font=font, fontsize=self.metrix.fontSize,
                            lineSpacing=self.metrix.lineSpacing)

            variablebox = (box[0], box[1] + r + 4, box[2], box[3])
            drawer.textarea(variablebox, texts[1],
                            fill=fill, halign='left', valign='top',
                            font=font, fontsize=self.metrix.fontSize,
                            lineSpacing=self.metrix.lineSpacing)


def setup(self):
    install_renderer('class', Class)
