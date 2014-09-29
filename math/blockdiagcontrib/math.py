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

from subprocess import Popen, PIPE
from shutil import rmtree
from errno import ENOENT
from tempfile import NamedTemporaryFile, mkdtemp
from blockdiag import plugins
from blockdiag.utils import unquote
from blockdiag.utils.logging import warning

formula_images = []

def get_latex_source(formula, env):
    return r'''
    \documentclass[12pt]{article}
    \usepackage[utf8x]{inputenc}
    \usepackage{amsmath}
    \usepackage{amsthm}
    \usepackage{amssymb}
    \usepackage{amsfonts}
    \usepackage{bm}
    \pagestyle{empty}
    \begin{document}
    \begin{%(env)s}
        %(formula)s
    \end{%(env)s}
    \end{document}
    ''' %{'formula':formula, 'env':env}


class FormulaImagePlugin(plugins.NodeHandler):
    def __init__(self, diagram, **kw):
        super(FormulaImagePlugin, self).__init__(diagram, **kw)
        self._env = kw.get('env', 'align*')


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
            formula = formula.strip()

            # create source .tex file
            source = NamedTemporaryFile(mode='w+b', suffix='.tex',
                                        dir=tmpdir, delete=False)
            latex_source = get_latex_source(formula, self._env).encode('utf-8')
            source.write(latex_source)
            # source.write((LATEX_SOURCE % formula).encode('utf-8'))
            source.close()

            # execute platex
            try:
                error = None
                args = ['platex', '--interaction=nonstopmode', source.name]
                latex = Popen(args, stdout=PIPE, stderr=PIPE, cwd=tmpdir)
                stdout, _ = latex.communicate()
                if latex.returncode != 0:
                    warning("raise LaTeX Exception:\n\n%s" %
                            stdout.decode('utf-8'))
                    return None
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
                stdout, _ = dvipng.communicate()
                if latex.returncode != 0:
                    warning("raise dvipng Exception:\n\n%s" %
                            stdout.decode('utf-8'))
                    return None
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
