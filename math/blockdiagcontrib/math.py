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

import re
import os.path
from subprocess import Popen, PIPE
from shutil import rmtree
from errno import ENOENT
from tempfile import NamedTemporaryFile, mkdtemp
from blockdiag import plugins
from blockdiag.utils import unquote
from blockdiag.utils.images import get_image_size
from blockdiag.utils.logging import warning

DEFAULT_ENVIRONMENT = 'align*'

LATEX_SOURCE = r'''
\documentclass[12pt]{article}
\usepackage[utf8x]{inputenc}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{bm}
%(usepackage)s
\pagestyle{empty}
\begin{document}
\begin{%(formula_env)s}
    %(formula)s
\end{%(formula_env)s}
\end{document}
'''

formula_images = []


def get_latex_source(formula, env, stylepackage):
    if stylepackage:
        usepackage = '\\usepackage{%s}\n' % stylepackage
    else:
        usepackage = ''

    return LATEX_SOURCE % {'formula': formula.strip(),
                           'formula_env': env,
                           'usepackage': usepackage}


class FormulaImagePlugin(plugins.NodeHandler):
    def __init__(self, diagram, **kwargs):
        super(FormulaImagePlugin, self).__init__(diagram, **kwargs)
        self.default_formula_env = kwargs.get('env', DEFAULT_ENVIRONMENT)
        self.stylepackage = None

        stylefile = kwargs.get('style')
        if stylefile:
            basedir = os.path.dirname(os.path.abspath(self.config.input))
            stylepath = os.path.join(basedir, stylefile)
            if os.path.exists(stylepath):
                # stylename exists on relative path from source file
                self.stylepackage = os.path.splitext(stylepath)[0]
            else:
                warning('stylefile not found: %s' % stylefile)

    def get_formula_env(self, uri):
        match = re.search(r'^math(?:\+([^/:]+))?://', uri)
        if not match:
            return None
        elif match.group(1):
            return match.group(1)
        else:
            return self.default_formula_env

    def on_created(self, node):
        node.resizable = False

    def on_attr_changing(self, node, attr):
        value = unquote(attr.value)

        if attr.name == 'background':
            return self.on_background_changing(node, value)
        elif attr.name == 'resizable':
            return self.on_resizable_changing(node, value)
        elif attr.name == 'label':
            return self.on_label_changing(node, value)
        else:
            return True

    def on_label_changing(self, node, value):
        formula_env = self.get_formula_env(value)
        if formula_env is None:  # not math uri
            return True

        if getattr(node, 'uses_formula_image', False):
            warning('formula has already been specified: %s' % value)
            return False

        node.label = ""
        return self.set_formula_image_to_background(node, value, formula_env)

    def on_background_changing(self, node, value):
        formula_env = self.get_formula_env(value)
        if formula_env is None:  # not math uri
            return True

        warning('background = "math://..." is deprecated. '
                'use label attribute.')
        return self.set_formula_image_to_background(node, value, formula_env)

    def on_resizable_changing(self, node, value):
        if value.lower() not in ('true', 'false'):
            warning('%s is not boolean value. ignored.' % value)

        if value.lower() == 'true':
            node.resizable = True
        else:
            node.resizable = False

        return False

    def on_build_finished(self, node):
        uses_formula_image = getattr(node, 'uses_formula_image', False)
        if uses_formula_image and node.resizable is True:
            node.width, node.height = get_image_size(node.background.name)

    def set_formula_image_to_background(self, node, value, formula_env):
        formula = value.split('://', 1)[1]
        image = self.create_formula_image(formula, formula_env)
        if image:
            formula_images.append(image)
            node.background = image
            node.uses_formula_image = True
        else:
            node.background = None

        return False

    def create_formula_image(self, formula, formula_env):
        try:
            tmpdir = mkdtemp()

            # create source .tex file
            source = NamedTemporaryFile(mode='w+b', suffix='.tex',
                                        dir=tmpdir, delete=False)
            latex_source = get_latex_source(formula, formula_env,
                                            self.stylepackage)
            source.write(latex_source.encode('utf-8'))
            source.close()

            # execute platex
            try:
                # `-no-shell-escape` blocks to invoke any commands
                args = ['platex', '--interaction=nonstopmode',
                        '-no-shell-escape', source.name]
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

                warning("Fail to convert formula: %s (reason: %s)" %
                        (formula, error))
                return None

            # execute dvipng
            try:
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
