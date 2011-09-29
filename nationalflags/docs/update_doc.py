#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

WIDTH = 2


def to_classname(filename):
    #137px-Flag_of_Lithuania.svg.png 
    filename = re.sub('.svg.png', '', filename)
    filename = re.sub('.*Flag_of_', '', filename)
    filename = re.sub('-', '_', filename)

    return "nationalflag.%s" % filename.lower()


def print_manual_headers():
    readme = os.path.join(os.path.dirname(__file__), '../README.txt')
    print open(readme).read()

    print ""

    print "Shapes"
    print "======="
    print ""


print_manual_headers()

print ".. list-table::"
print "   :header-rows: 0"

path = "%s/../blockdiagcontrib/images/nationalflags" % os.path.dirname(__file__)
dir = os.listdir(path)
for i, filename in enumerate(dir):
    shape = to_classname(filename)

    if i % WIDTH == 0:
        print ""
        print "   * - shape = \"%s\"" % shape
    else:
        print ""
        print "     - shape = \"%s\"" % shape

    print ""
    print "       .. blockdiag::"
    print ""
    print "          { A [label = \"\", shape = \"%s\"]; }" % shape

if i % WIDTH != (WIDTH - 1):
    for j in range(i % WIDTH, WIDTH - 1):
        print "     -"
