=====================
blockdiagcontrib-math
=====================
A plugin for `blockdiag` that provides LaTeX math as background of nodes.

examples
=========
`blockdiagcontrib-math` detects background attribute starts with 'math://',
and converts it as math formula using LaTeX and dvipng.

Example::

   blockdiag {
     plugin math;
     A [label = "", background = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

.. blockdiag::

   blockdiag {
     plugin math;
     A [label = "", background = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

change style of formula
========================
`blockdiagcontrib-math` supports applying user defined style::

   blockdiag {
     plugin math[style = "mystyle.sty"];
     A [label = "", background = "math://\int_{0}^{\infty} f(x)dx"];
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
        plugin math[env = "eqnarray"];
        A [label = "", background = "math://\int_{0}^{\infty} f(x)dx"];
        A -> B;
      }

Change environment per node

    Declare any environmet as URI schema. it changes formula environment per node::

      blockdiag {
        plugin math
        A [label = "", background = "math+eqnarray://\int_{0}^{\infty} f(x)dx"];
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
