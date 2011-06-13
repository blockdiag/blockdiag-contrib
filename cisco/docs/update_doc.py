#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

WIDTH = 3


def to_classname(filename):
    filename = re.sub('\.[a-z]+$', '', filename)
    filename = re.sub(' ', '_', filename)

    return "cisco.%s" % filename


print ".. list-table::"
print "   :header-rows: 0"

path = "%s/../blockdiagcontrib/images/cisco" % os.path.dirname(__file__)
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
    print "          { A [label = '', shape = '%s']; }" % shape

if i % WIDTH != (WIDTH - 1):
    for j in range(i % WIDTH, WIDTH - 1):
        print "     -"
