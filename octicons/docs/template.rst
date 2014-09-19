=========================
blockdiagcontrib-octicons
=========================
A plugin for `blockdiag` that provides octicons as background/icon of nodes.

examples
=========
`blockdiagcontrib-octicons` detects background and icon attributes starts with 'octicon://',
and converts it as octicons_ .

.. _octicons: https://octicons.github.com/

Example::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github"];
     B [icon = "octicon://cloud-upload?color=red"];
     A -> B;
   }

.. blockdiag::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github"];
     B [icon = "octicon://cloud-upload?color=red"];
     A -> B;
   }

see results at http://pythonhosted.org//blockdiagcontrib-octicons/

Requirements
============
* blockdiag 1.4.3 or later

Copyright of octicons.ttf
=========================
\(c) 2012-2014 GitHub

License
=======
Apache License 2.0

.. note::

   octicons.ttf is licensed under SIL OFL 1.1 (http://scripts.sil.org/OFL)

Usage
=====

At first, load `octicons` plugin with plugin statement.
And then, you can use `octicon://` URI to background and icon attributes::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github"];
   }

`octicon://` URI accepts two options: size and color

`color` option changes color of octicon::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?color=red"];
   }

.. blockdiag::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?color=red"];
   }

`size` option changes size of octicon. you can choose from large, normal, small and pixels::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?size=large"];
     B [label = "", background = "octicon://mark-github?size=normal"];
     C [label = "", background = "octicon://mark-github?size=small"];
     D [label = "", background = "octicon://mark-github?size=8"];
   }

.. blockdiag::

   blockdiag {
     plugin octicons;

     A [label = "", background = "octicon://mark-github?size=large"];
     B [label = "", background = "octicon://mark-github?size=normal"];
     C [label = "", background = "octicon://mark-github?size=small"];
     D [label = "", background = "octicon://mark-github?size=8"];
   }

name of octicons
=================

