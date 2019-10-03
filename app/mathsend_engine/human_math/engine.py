from sympy import *
from sympy.abc import *
from . import substandard



def convert(inp):
    """
    Since human readable expressions ofen combine numeric with alphabet
    when they are meant to be multiplied, Thus,
    all equations must be re-written to place * between then.
    For example: 5x+8sin(x) means 5*x+8*sin(x)
    """
    # Is there "=" in the expresion?"
    if len(inp) == 0:
        return inp

    # Rewrite the expression from scratch
    tmp = [inp[0]]
    for i in range(1, len(inp)):
        # '*' should only be written if a digit and alphabet are next to each other
        if (inp[i].isalpha() and inp[i - 1].isdigit()) or (
            inp[i].isdigit() and inp[i - 1].isalpha()):
            tmp.append('*')
        tmp.append(inp[i])
    ans = ''.join(tmp)
    return ans

def equate(inexpr):
    # Negating the RHS
    left, right = inexpr.split('=', 1)
    ans = '{}-({})'.format(left, right)
    return ans


def rewrite(in_expr):
    """
    This function generate the python equivalent of a
    human readable expression
    """
    # norm_input substitutes some allowed sub-standard operators
    norm_in = substandard.norm_input(str(in_expr).lower())
    norm_in = convert(norm_in)
    if '=' in norm_in:
        norm_in = equate(norm_in)
    return norm_in

def compute(in_expr):
    try:
        # checking if it's one of the supported casual texts
        comval = substandard.my_texts[str(in_expr).lower()]
        return comval
    except:
        pass
    # Standardize the expression
    norm_in = rewrite(in_expr)

    try:
        """
        checking if the starts with an operation key word
        such as differentiate(2x+9)
        in order not to capture some standard short math functions as
        an operation key word, such as sin(), cos(), a rule of thumb that if the first word before "("
        is not an operation keyword if its not longer than 3
        
        the solve operation is tried on the incoming expression"""
        parts = norm_in.split("(")
        if parts[0].isalpha() and len(parts[0])>3:
                raise Exception
        comval = solve(norm_in)
        if len(comval) ==0:
            raise Exception

    except:
        try:
            """
            try to solve symbolically first, and it will
            produce whole number for multiplication
            """
            comval = sympify(norm_in)

            try:
                float(comval) #it will not float if its not purely numeric
                full_expr = "(" + norm_in + ")" + ".evalf(6)"
                comval2 = sympify(full_expr)
                # trailing zeros are not needed for something like 6*5=30
                if comval != comval2:
                    comval = comval2

            except:
                pass

        except:
            comval = substandard.my_texts["errortxt"]
    # converting the solution back to human readable form       
    comval = str(comval)
    comval = comval.replace("**","^")
    comval = comval.replace("oo","inf")
    return comval

