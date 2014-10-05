# -*- coding: utf-8 -*-

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from blockdiagcontrib.math import get_latex_source


class TestBlockdiagcontribMath(unittest.TestCase):
    def test_get_latex_source(self):
        # normal case
        source = get_latex_source('formula', 'myenv', None)
        self.assertIn('\\begin{myenv}\n    formula\n\\end{myenv}', source)

        # formula with spaces
        source = get_latex_source('  \n\n   formula\n\n  ', 'myenv', None)
        self.assertIn('\\begin{myenv}\n    formula\n\\end{myenv}', source)

        # specify style package
        source = get_latex_source('formula', 'myenv', 'mystyle')
        self.assertIn('\\usepackage{mystyle}\n', source)
        self.assertIn('\\begin{myenv}\n    formula\n\\end{myenv}', source)
