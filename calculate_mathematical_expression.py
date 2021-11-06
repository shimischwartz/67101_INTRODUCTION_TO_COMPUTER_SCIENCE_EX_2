#################################################################
#FILE: calculate_mathematical_expression.py
#WRITER: shimon_schwartz , shimioschwartz , 201572807
#EXERCIS: intro2cs1 ex2 2018-2019
#DESRIPTION:a programe that receives a text message with a simple
# math question and returns the calculated value of the expression
#################################################################


def calculate_mathematical_expression(num1, num2, calc):
    """a fFunction that makes simple calculations"""
    if calc == "/" and num2 != 0:
        return num1/num2
    elif calc == "+":
        return num1+num2
    elif calc == "-":
        return num1-num2
    elif calc == "*":
        return num1*num2
    else:
        return None


def calculate_from_string(sms):
    # a function that receives a text message with a simple math
    # question and returns the calculated value of the expression
    # by using the previous function
    num1, calc, num2 = sms.split()
    num1 = float(num1)
    num2 = float(num2)
    return calculate_mathematical_expression(num1, num2, calc)
