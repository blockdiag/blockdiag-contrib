======================
blockdiagcontrib-cisco
======================
A plugin for `blockdiag` that provides shapes for networking.
The shapes are using `Network Topology Icons`_ designed by `Cisco Systems, Inc`_ .

.. _Network Topology Icons: http://www.cisco.com/web/about/ac50/ac47/2.html
.. _Cisco Systems, Inc: http://www.cisco.com/

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
