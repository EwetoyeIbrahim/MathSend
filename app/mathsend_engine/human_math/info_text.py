# -*- coding: utf-8 -*-

abouttxt = " I am a Mathematician created by EWETOYE Ibrahim to handle mathematics on social media platforms."

errortxt = " Unknown Expression, use 'help' if you need it"

helptxt = """
***********
Solve Keywords

Solve()
formats:
solve(expression)
solve(expression, variable)
solve([expression1, expression2],[var1,var2])
Expressions are assumed to be equal to zero. In case of numerous variables, the variable to be solved for may be specified, else one will be chosen automatically, usually x if present. For example: solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])

***********
Simplification Keywords

Expand():
Given an expression that conforms to the form like: (ax+b)^n The "elementary" method is to write the expression within the bracket n times.
For example, expand((2*x+3)^2; expand((3x-7)^9)

Factor():
For a factorization operation to be referred to as successful, the resulting form must be further irreducible. For example, factor(x^4 - 3*x^2 + 1)

Collect():
whenever you only need polynomial coefficients and not the full expression, the collect keyword takes care of that. It must be noted that the reported solution will be in descending power of the variable where the missing powers are represented with zero. For example, it's obvious that the coefficient of collect(11x^4 - 36x^3+x +3) yields [11 -36 0 1 3].

Cancel():
Given a rational expression a/b, the cancel keyword tries to cancel-out all common factors in the supplied fraction to give an irreducible rational expression as x/y. For example, 18/12, the common factor is 6 which reduces the the rational function to 3/2.

APART():
for any given rational function, MATHSEND compute the partial fraction decomposition of the function when supplied with the apart keyword.

Trigsimplify():
used to convert trigonometric expressions to their simplest and smallest reducible terms. Just as factor is to polynomial expression, the output of the operation will be the smallest irreducible form of the supplied expression. For example: trigsimplify(sin(x)^2+cos(x)^2) = 1

Trigexpand():
It's the opposite of trigsimp and the trigonometric counter part the Expand() keyword for trigonometric function.

Simplify():
supplying an expression this keyword forces MATHSEND to apply several methods to the expression in order to comeup with a reasonable simplified solution. For example: simplify(2x^2 + 3x + 4x) = x*(2*x + 7)

***********
Calculus Operations
***********
Differentiate()
differentiate(expression)
differentiate(expression, var)
For example: differrentiate(sin(x)*exp(x)); differentiate(2x*y^2 + 3y + z,y) will yield a solution with respect to y... read more at mathsend.com/help
Integrate()
integrate(expression)
integrate(expression, variable)
integrate(expression, variable, lower_limit, upper_limit)
For example, integrate(3*y*x^4+8y) will integrate expression with respect to x; integrate(3*y/x^4+8y*x*z, y) will integrate with respect to y; integrate integrate(3*y/x^4+8yxz, y, x,x,z) integrates the expression four times; integrate(3*y/x^4+8yxz, y, 0, inf) will integrate the expression with respect to y from 0 to infinity

Limit()
limit(expression)
limit(expression, variable)
limit(expression, variable, lower_limit, upper_limit)
The format is limit(expression, variable, lower_limit, upper_limit). For example: limit(x*sin(1/x), x, inf)

Series()
series(expression)
series(expression, variable)
series(expression, variable, x0, upper_limit)
if the x0 and order values are not specified (that is, any of the first two formats) x0 will be taken as 0 while the order as 6. For example: series(sin(x)) computes the Taylor series of sin(x) up to the order of series; and for a higher order of the series, say 9, use series(sin(x),0,9).
"""