**Human Readable Calculator**
Human math is a simple symbolic calculator. It collects equations in human readable form; rewrites it in Python syntax and then, optional, feeds it into sympy for computation.
It must be noted that __version 1.0.0__ only supports string input and output.

HumanMath.express("expression") returns simply converts from human readable format to python expression solvable with at least sympy module

HumanMath.compute("expression") solves human readable expression symbolically with sympy module.