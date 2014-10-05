# -*- coding: utf-8 -*-
from blockdiag.noderenderer.box import Box
from blockdiag.noderenderer import install_renderer
from blockdiag.utils import XY
from blockdiag.imagedraw.simplesvg import pathdata


class QB(Box):
    def render_shape(self, drawer, format, **kwargs):
        super(QB, self).render_shape(drawer, format, **kwargs)

        outline = kwargs.get('outline')
        fill = kwargs.get('fill')

        # draw outline
        if not kwargs.get('shadow'):
            m = self.metrics
            h = m.node_height / 4
            w = m.node_width / 6
            r = m.cellsize

            # left eye
            xy = self.metrics.cell(self.node).top
            left = XY(xy.x - w, xy.y + h)
            self.render_eye(drawer, left)

            # right eye
            right = XY(xy.x + w, xy.y + h)
            self.render_eye(drawer, right)

            # left mouthline
            xy = self.metrics.cell(self.node).bottom
            y = xy.y - h * 3 / 2 + r / 2

            if w > r * 3:
                rx = r * 3
                ry = r * 3 / 4
            else:
                rx = w - r
                ry = r / 2

            if format == 'SVG':
                path = pathdata(xy.x - rx, y)
                path.ellarc(rx / 2, ry, 0, 0, 0, xy.x, y)
                path.ellarc(rx / 2, ry, 0, 0, 0, xy.x + rx, y)

                drawer.path(path, fill="none", outline=fill)
            else:
                box = (xy.x - rx, y - ry, xy.x, y + ry)
                drawer.arc(box, 0, 180, fill=fill)

                box = (xy.x, y - ry, xy.x + rx, y + ry)
                drawer.arc(box, 0, 180, fill=fill)

    def render_eye(self, drawer, center):
        m = self.metrics

        r = m.cellsize
        eye = (center.x - r, center.y - r, center.x + r, center.y + r)
        drawer.ellipse(eye, fill='orange', outline='orange')

        r = m.cellsize * 2 / 3
        eye = (center.x - r, center.y - r, center.x + r, center.y + r)
        drawer.ellipse(eye, fill='red', outline='red')

        r = m.cellsize / 3
        eye = (center.x + r, center.y - r * 3, center.x + r * 3, center.y - r)
        drawer.ellipse(eye, fill='white', outline='white')


def setup(self):
    install_renderer('qb', QB)
    install_renderer('QB', QB)
