=====================
blockdiagcontrib-math
=====================
A plugin for `blockdiag` that provides LaTeX math as background of nodes.

examples
=========
`blockdiagcontrib-math` detects label or background attribute starts with 'math://',
and converts it as math formula using LaTeX and dvipng.

Example::

   blockdiag {
     plugin math;
     A [label = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

And the following code has mean same as an above code.

Example::

   blockdiag {
     plugin math;
     A [label="", background = "math://\int_{0}^{\infty} f(x)dx"];
     A -> B;
   }

see results at http://pythonhosted.org//blockdiagcontrib-math/

Requirements
============
* blockdiag 1.4.2 or later
* LaTeX
* dvipng

LaTeX Packages
--------------

* `amsmath`
* `amsthm`
* `amssymb`
* `amsfonts`
* `bm`

License
=======
Apache License 2.0
