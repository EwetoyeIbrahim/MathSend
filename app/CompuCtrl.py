#from __main__ import *
from __future__ import division
from sympy import *
from sympy.abc import *
from app.substandard import my_texts, norm_input


class CompuCtrl:

    def format_equation(self, inp_str):
        lst = str("".join([c + "*" if (c.isnumeric() and d.isalpha()) else (c+"*" if (c.isalpha() and d.isnumeric()) else c) for c,d in zip(inp_str,inp_str[1:])]) + inp_str[-1]).split("=")
        lhs = lst[0]
        rhs = "+" + str(abs(int(lst[1]))) if int(lst[1]) <0 else "-" + str(lst[1])
        return lhs + rhs

    def convert(self, inp):
        # Edge case check
        if len(inp) == 0: return inp

        # Go through the string looking for where to place '*'s
        # Add the first character
        tmp = [inp[0]]
        for i in range(1, len(inp)):
            # If letter followed by digit or the reverse, then add a '*'
            if (inp[i].isalpha() and inp[i - 1].isdigit()) or (inp[i].isdigit() and inp[i - 1].isalpha()):
                tmp.append('*')
            # Now add the current character
            tmp.append(inp[i])
        # Convert the resulting list back to a string
        ans = ''.join(tmp)

        # Now if the equal sign is present, split the result
        # and negate the right hand side
        if '=' in ans:
            left, right = ans.split('=', 1)
            ans = '{}-({})'.format(left, right)

        # Return the answer
        return ans


    def norm_in(self, in_expr):
        in_expr = self.convert(in_expr)
        norm_in = in_expr.lower()
        norm_in = norm_input(norm_in)
        return norm_in

    def compu(self, in_expr):
        norm_in = self.norm_in(in_expr)
        norm_expr = "(" + norm_in + ")"
        try:
            comval = my_texts[norm_in]
            return comval
        except:
            pass

        try:
            parts = norm_in.split("(")
            if parts[0].isalpha() and len(parts[0])>3:
            	    raise Exception
            comval = solve(norm_in)
            if len(comval) ==0:
                raise Exception

        except:
            try:
                '''try to solve symbolically first, and it will
                produce whole number for multiplication'''
                comval = sympify(norm_in)

                try:
                    float(comval) #it will not float if its not purely numeric
                    full_expr = norm_expr + ".evalf(6)"
                    comval2 = sympify(full_expr)

                    if comval != comval2:
                        comval = comval2

                except:
                    pass

            except:
                try:
                    comval = solve(norm_in)
                    if len(comval) ==0:
                        raise Exception

                except:

                    comval = my_texts["errortxt"]
        comval = str(comval)



        comval = str(comval)
        comval = comval.replace("**","^")
        comval = comval.replace("oo","inf")
        return comval

if __name__ == '__main__':
    CompuCtrl()
