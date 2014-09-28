#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, '..')
from blockdiagcontrib import octicons

WIDTH = 3


# print header
print open('template.rst').read()

print ".. list-table::"
print "   :header-rows: 0"

for i, iconname in enumerate(octicons.icons.keys()):
    uri = 'octicon://%s' % iconname
    if i % WIDTH == 0:
        print ""
        print "   * - %s" % uri
    else:
        print ""
        print "     - %s" % uri

    print ""
    print "       .. blockdiag::"
    print ""
    print "          { plugin octicons; A [label = '', background = '%s']; }" % uri

if i % WIDTH != (WIDTH - 1):
    for j in range(i % WIDTH, WIDTH - 1):
        print "     -"
