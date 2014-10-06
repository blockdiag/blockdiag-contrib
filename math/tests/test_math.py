# -*- coding: utf-8 -*-

import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

import os
from shutil import rmtree
from tempfile import mkdtemp
from collections import namedtuple
from blockdiagcontrib.math import get_latex_source, FormulaImagePlugin


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

    def test_FormulaImagePlugin_init(self):
        Config = namedtuple('Config', 'input')
        try:
            curdir = os.getcwd()
            tmpdir = mkdtemp()
            os.chdir(tmpdir)
            tmpdir = os.getcwd()   # for MacOSX; tmpdir is based on symlinks

            # normal case
            plugin = FormulaImagePlugin(None)
            self.assertEqual('align*', plugin.default_formula_env)
            self.assertEqual(None, plugin.stylepackage)

            # specify env
            plugin = FormulaImagePlugin(None, env='myenv')
            self.assertEqual('myenv', plugin.default_formula_env)
            self.assertEqual(None, plugin.stylepackage)

            # specify style file (same directory)
            path = '%s/mystyle.sty' % tmpdir
            open(path, 'wt').close()  # create dummy file
            plugin = FormulaImagePlugin(None,
                                        config=Config('src.diag'),
                                        style='mystyle.sty')
            self.assertEqual('align*', plugin.default_formula_env)
            self.assertEqual(os.path.splitext(path)[0], plugin.stylepackage)

            # specify style file (different directory)
            plugin = FormulaImagePlugin(None,
                                        config=Config('subdir/src.diag'),
                                        style='mystyle.sty')
            self.assertEqual('align*', plugin.default_formula_env)
            self.assertEqual(None, plugin.stylepackage)

            # specify style file (abspath)
            plugin = FormulaImagePlugin(None,
                                        config=Config('subdir/src.diag'),
                                        style=path)
            self.assertEqual('align*', plugin.default_formula_env)
            self.assertEqual(os.path.splitext(path)[0], plugin.stylepackage)

            # specify style file (not exist)
            plugin = FormulaImagePlugin(None,
                                        config=Config('/path/to/src.diag'),
                                        style='mystyle.sty')
            self.assertEqual('align*', plugin.default_formula_env)
            self.assertEqual(None, plugin.stylepackage)
        finally:
            os.chdir(curdir)
            rmtree(tmpdir)
