===============================
blockdiagcontrib-nationalflags
===============================
A plugin for `blockdiag` that provides shapes for national-flags.
The shapes are using `National Flags`_ images provided by `Wikipedia`_ .

.. _National Flags: http://ja.wikipedia.org/wiki/%E5%9B%BD%E6%97%97%E3%81%AE%E4%B8%80%E8%A6%A7
.. _Wikipedia: http://www.wikipedia.org/

Diagram examples
================
`blockdiagcontrib-nationalflags` renders network icon as node's shape.

Example::

   diagram admin {
     A [shape = "nationalflag.japan"];
   }

.. blockdiag::

   diagram admin {
     A [shape = "nationalflag.japan"];
   }

Or, use `shape_namespace` keyword::

   diagram admin {
     shape_namespace = "nationalflag";

     A [shape = "japan"];
   }

.. blockdiag::

   diagram admin {
     shape_namespace = "nationalflag";

     A [shape = "japan"];
   }

See more examples and output images in http://packages.python.org/blockdiagcontrib-nationalflags/ .


Requirements
============
* blockdiag 0.9.1 or later


License
=======
Python Software Foundation License.
