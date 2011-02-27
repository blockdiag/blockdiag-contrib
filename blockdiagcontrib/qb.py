# -*- coding: utf-8 -*-
from blockdiag.noderenderer.box import Box
from blockdiag.noderenderer import install_renderer
from blockdiag.utils.XY import XY
from blockdiag.SVGdraw import pathdata


class QB(Box):
    def render_shape(self, drawer, format, **kwargs):
        super(QB, self).render_shape(drawer, format, **kwargs)

        outline = kwargs.get('outline')
        fill = kwargs.get('fill')

        # draw outline
        if not kwargs.get('shadow'):
            m = self.metrix
            h = m.nodeHeight / 4
            w = m.nodeWidth / 6
            r = m.cellSize

            # left eye
            xy = self.metrix.cell(self.node).top()
            left = XY(xy.x - w, xy.y + h)
            self.render_eye(drawer, left)

            # right eye
            right = XY(xy.x + w, xy.y + h)
            self.render_eye(drawer, right)

            # left mouthline
            xy = self.metrix.cell(self.node).bottom()
            y = xy.y - h * 3 / 2 + r / 2

            if w > r * 3:
                rx = r * 3
                ry = r * 3 / 4
            else:
                rx = w - r
                ry = r / 2

            path = pathdata(xy.x - rx, y)
            path.ellarc(rx / 2, ry, 0, 0, 0, xy.x, y)
            path.ellarc(rx / 2, ry, 0, 0, 0, xy.x + rx, y)

            drawer.path(path, fill="none", outline=fill)

    def render_eye(self, drawer, center):
        m = self.metrix

        r = m.cellSize
        eye = (center.x - r, center.y - r, center.x + r, center.y + r)
        drawer.ellipse(eye, fill='orange', outline='orange')

        r = m.cellSize * 2 / 3
        eye = (center.x - r, center.y - r, center.x + r, center.y + r)
        drawer.ellipse(eye, fill='red', outline='red')

        r = m.cellSize / 3
        eye = (center.x + r, center.y - r * 3, center.x + r * 3, center.y - r)
        drawer.ellipse(eye, fill='white', outline='white')


def setup(self):
    install_renderer('qb', QB)
