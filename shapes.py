###############################################################
#FILE: shapes.py
#WRITER: shimon_schwartz , shimioschwartz , 201572807
#EXERCIS: intro2cs1 ex2 2018-2019
#DESRIPTION:a program#  that receives a frome the user shape and
# sizes accordingly, and returns the space
# P.S. Works only with circles, rectangles and Triangular
# equilateral triangles
#################################################################

import math


def circle_area():
    # A function that calculates a circle area
    radius = input()
    radius = float(radius)
    c_area = radius ** 2 * math.pi
    return c_area


def rectangle_area():
    # A function that calculates the area of a rectangle
    rib1 = input()
    rib2 = input()
    rib1 = float(rib1)
    rib2 = float(rib2)
    rect_area = rib1 * rib2
    return rect_area


def triangle_area():
    # A function that calculates the area of an equilateral triangle
    side = input()
    side = float(side)
    tri_area = (math.pow(side, 2) * math.sqrt(3))/4
    return tri_area


def shape_area():
    # a function that receives a from the user shape and sizes
    # accordingly, and returns the space By using the functions above
    ans1 = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    ans1 = float(ans1)
    if ans1 != 1 and ans1 != 2 and ans1 != 3:
        return None
    elif ans1 == 1:
        return circle_area()
    elif ans1 == 2:
        return rectangle_area()
    else:
        return triangle_area()


if __name__ == "__main__":
    print(shape_area())