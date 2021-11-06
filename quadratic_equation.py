###############################################################
#FILE: quadratic_equation.py
#WRITER: shimon_schwartz , shimioschwartz , 201572807
#EXERCIS: intro2cs1 ex2 2018-2019
#DESRIPTION: A code that receives from the user coefficients of
# a quadratic equation and returns a solution respectively
#################################################################

import math


def quadratic_equation(a, b, c):
    # a function that can be called with coefficients of a quadratic
    # equation and returns a solution accordingly
    delta = float(b**2-4*a*c)
    ans1 = (-b + delta**(1/2))/(2*a)
    ans2 = (-b-delta**(1/2))/(2*a)

    if delta > 0:
        return ans1, ans2
    elif delta == 0:
        return ans1, None
    else:
        return None, None


def quadratic_equation_user_input():
    # a function that receives from the user coefficients of a
    # quadratic equation and prints a solution accordingly
    nmn = input("Insert coefficients a, b, and c: ")
    a, b, c = nmn.split()
    a = float(a)
    b = float(b)
    c = float(c)
    ans1, ans2 = (quadratic_equation(a, b, c))
    if ans1 is None:
        print("The equation has no solutions")
    elif ans2 is not None:
        print("The equation has 2 solutions:", ans1, "and", ans2)
    else:
        print("The equation has 1 solution:", ans1)

