======================
blockdiagcontrib-cisco
======================
A plugin for `blockdiag` that provides node-renderers for networking

Diagram examples
================
`blockdiagcontrib-cisco` renders network icon as node's shape.

Example::

   diagram admin {
     A [shape = "cisco.router"];
   }

.. blockdiag::

   diagram admin {
     A [shape = "cisco.router"];
   }

Or, use `shape_namespace` keyword::

   diagram admin {
     shape_namespace = "cisco";

     A [shape = "router"];
   }

.. blockdiag::

   diagram admin {
     shape_namespace = "cisco";

     A [shape = "router"];
   }

See more examples and output images in http://packages.python.org/blockdiagcontrib-cisco/ .


Requirements
============
* blockdiag 0.8.0 or later


License
=======
Python Software Foundation License.
