###############################################################
#FILE: temperature.py
#WRITER: shimon_schwartz , shimioschwartz , 201572807
#EXERCIS: intro2cs1 ex2 2018-2019
#DESRIPTION: a program that receives a certain threshold and a
# temperature of three days and returns if in two of the
# three days the temperature was higher than the threshold
#################################################################


def is_it_summer_yet(min_temp, day1, day2, day3):
    # a function that receives a certain threshold and a temperature of three
    # days and returns if in two of the three days the temperature
    # was higher than the threshold
    if min_temp < day1 and min_temp < day2:
        return True
    elif min_temp < day1 and min_temp < day3:
        return True
    elif min_temp < day2 and min_temp < day3:
        return True
    elif min_temp < day1 and min_temp < day2:
        return True
    else:
        return False