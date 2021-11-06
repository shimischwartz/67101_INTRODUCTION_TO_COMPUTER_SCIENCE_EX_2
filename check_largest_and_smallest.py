#################################################################
#FILE:check_largest_and_smallest.py
#WRITER:shimon_schwartz , shimioschwartz , 201572807
#EXERCIS:intro2cs1 ex2 2018-2019
#DESRIPTION:a programe that checks the function:
# "largest_and_smallest" from above
#################################################################

from largest_and_smallest import largest_and_smallest


def test_largest_and_smallest():
    # A function that checks the function: "largest_and_smallest" from above
    if largest_and_smallest(3, 2, 1) == (3, 1) and \
        largest_and_smallest(3, 1, 2) == (3, 1) and \
        largest_and_smallest(2, 3, 1) == (3, 1) and \
        largest_and_smallest(2, 1, 3) == (3, 1) and \
            largest_and_smallest(1, 2, 3,) == (3, 1):

        print("function largest_and_smallest test success")
        return True
    else:
        print("function largest_and_smallest test fail")
        return False


if __name__ == "__main__":
    test_largest_and_smallest()