#################################################################
#FILE: largest_and_smallest.py
#WRITER: shimon_schwartz , shimioschwartz , 201572807
#EXERCIS: intro2cs1 ex2 2018-2019
#DESRIPTION:a programe which accepts three numeric values and
#returns two values - the largest and the smallest
#################################################################


def largest_and_smallest(n1, n2, n3):
    # A function that accepts three numeric values and returns two
    #  values - the largest and the smallest
        if n1 >= n2:
            if n3 >= n1:
                return n3, n2
            elif n3 <= n2:
                return n1, n3
            else:
                return n1, n2

        if n1 < n2:
            if n3 >= n2:
                return n3, n1
            elif n3 >= n1:
                return n2, n1
            else:
                return n2, n3
