
# -*- coding: utf-8 -*-
import mathCal_

##输入参数为角度制

#计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def Calculate_sin(x):
    angle = math.radians(x)
    result = 0;
    for i in range(10):
        term = (-1)**i*angle**(2*i+1)/factorial(2*i+1)
        result += term
    return result


def Calculate_cos(x):
    angle = math.radians(x)
    result = 0;
    for i in range(10):
        term = (-1)**i*angle**(2*i)/factorial(2*i)
        result += term
    return result
    
def Calculate_tan(x):
    sin_result = Calculate_sin(x)
    cos_result = Calculate_cos(x)
    return sin_result / cos_result   
    

