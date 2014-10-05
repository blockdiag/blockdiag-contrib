# -*- coding: utf-8 -*-

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from blockdiagcontrib.math import get_latex_source


class TestBlockdiagcontribMath(unittest.TestCase):
    def test_get_latex_source(self):
        source = get_latex_source('formula', 'myenv')
        self.assertIn('\\begin{myenv}\n    formula\n\\end{myenv}', source)

        source = get_latex_source('  \n\n   formula\n\n  ', 'myenv')
        self.assertIn('\\begin{myenv}\n    formula\n\\end{myenv}', source)
