# -*- coding: utf-8 -*-
#  Copyright 2014 Takeshi KOMIYA
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

import os.path
from subprocess import Popen, PIPE
from shutil import rmtree
from errno import ENOENT
from tempfile import NamedTemporaryFile, mkdtemp
from blockdiag import plugins
from blockdiag.utils import unquote
from blockdiag.utils.logging import warning

STY_FILENAME = 'diag_math.sty'
STY_FILENAME = os.path.abspath(STY_FILENAME)

if os.path.exists(STY_FILENAME):
    including_package = '\\usepackage{%s}\n' % (
            os.path.splitext(STY_FILENAME)[0])
else:
    including_package = ''

LATEX_SOURCE = r'''
\documentclass[12pt]{article}
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{bm}
'''
LATEX_SOURCE += including_package
LATEX_SOURCE += r'''
\pagestyle{empty}
\begin{document}
\[
    {\Huge %s}
\]
\end{document}
'''

formula_images = []


class FormulaImagePlugin(plugins.NodeHandler):

    def on_attr_changing(self, node, attr):
        value = unquote(attr.value)
        if attr.name == 'background' and value.startswith('math://'):
            image = self.create_formula_image(value.replace('math://', ''))
            if image:
                formula_images.append(image)
                node.background = image
            else:
                node.background = None

            return False
        else:
            return True

    def create_formula_image(self, formula):
        try:
            tmpdir = mkdtemp()

            # create source .tex file
            source = NamedTemporaryFile(mode='w+b', suffix='.tex',
                                        dir=tmpdir, delete=False)
            source.write((LATEX_SOURCE % formula).encode('utf-8'))
            source.close()

            # execute platex
            try:
                error = None
                args = ['platex', '--interaction=nonstopmode', source.name]
                latex = Popen(args, stdout=PIPE, stderr=PIPE, cwd=tmpdir)
                stdout, stderr = latex.communicate()
                if latex.returncode != 0:
                    error = stdout
            except Exception as exc:
                if isinstance(exc, OSError) and exc.errno == ENOENT:
                    error = 'platex command not found'
                else:
                    error = exc

            if error:
                warning("Fail to convert formula: %s (reason: %s)" %
                        (formula, error))
                return None

            # execute dvipng
            try:
                error = None
                dvifile = source.name.replace('.tex', '.dvi')
                output = NamedTemporaryFile(suffix='.png')
                args = ['dvipng', '-gamma', '1.5',
                        '-D', '110', '-T', 'tight',
                        '-bg', 'Transparent', '-z0', dvifile,
                        '-o', output.name]
                dvipng = Popen(args, stdout=PIPE, stderr=PIPE, cwd=tmpdir)
                stdout, stderr = dvipng.communicate()
                if latex.returncode != 0:
                    error = stdout
            except Exception as exc:
                output.close()
                if isinstance(exc, OSError) and exc.errno == ENOENT:
                    error = 'dvipng command not found'
                else:
                    error = exc

            if error:
                output.close()
                warning("Fail to convert formula: %s (reason: %s)" %
                        (formula, error))
                return None

            return output
        finally:
            rmtree(tmpdir)


def on_cleanup():
    for image in formula_images[:]:
        image.close()
        formula_images.remove(image)


def setup(self, diagram, **kwargs):
    plugins.install_node_handler(FormulaImagePlugin(diagram, **kwargs))
    plugins.install_general_handler('cleanup', on_cleanup)
