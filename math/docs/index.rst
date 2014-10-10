=====================
blockdiagcontrib-math
=====================
A plugin for `blockdiag` that provides LaTeX math as background of nodes.

examples
=========
`blockdiagcontrib-math` detects label attribute starts with 'math://',
and converts it as math formula using LaTeX and dvipng.

Example::

   blockdiag {
     plugin math;
     A [label = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

.. blockdiag::

   blockdiag {
     plugin math;
     A [label = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

resize node to size of formula
===============================
`blockdiag-contrib-math` adds new node attribute named `resizable`.
If `true` is set, the plugin resizes node to size of formula automatically::

   blockdiag {
     plugin math;
     A [resizable = true, label = "math://\int_{0}^{\infty} f(x)dx"];
     B [resizable = true, label = "math://\int_{0}^{\infty} f(x)dx \\ \int_{0}^{\infty} f(y) dy"];
     A -> B;
   }

.. blockdiag::

   blockdiag {
     plugin math;
     A [resizable = true, label = "math://\int_{0}^{\infty} f(x)dx"];
     B [resizable = true, label = "math://\int_{0}^{\infty} f(x)dx \\ \int_{0}^{\infty} f(y) dy"];
     A -> B;
   }

.. note:: `resizable` attribute depends on blockdiag-1.4.5 or newer.

change style of formula
========================
`blockdiagcontrib-math` supports applying user defined style::

   blockdiag {
     plugin math[style = "mystyle.sty"];
     A [label = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

`blockdiagcontrib-math` searchs stylefile from same directory from source file.

change formula envrionment
===========================
`blockdiagcontrib-math` uses `align*` environment by default.

If you want to change formula environment to others,
there is two way to switch it.

Change default environment

   math plugin allows `env` option. it changes default formula environment::

      blockdiag {
        plugin math[env = "eqnarray*"];
        A [label = "math://\int_{0}^{\infty} f(x)dx"];
        A -> B;
      }

Change environment per node

    Declare any environmet as URI schema. it changes formula environment per node::

      blockdiag {
        plugin math
        A [label = "math+eqnarray*://\int_{0}^{\infty} f(x)dx"];
        A -> B;
      }


Requirements
============
* blockdiag 1.4.2 or later
* LaTeX
* dvipng

License
=======
Apache License 2.0
