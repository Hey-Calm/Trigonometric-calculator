
# -*- coding: utf-8 -*-

##输入参数为弧度制
import math
#计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def Calculate_sin(x):
    x=x%(2*math.pi)
    result = 0;
    for i in range(10):
        term = (-1)**i*x**(2*i+1)/factorial(2*i+1)
        result += term
    return result


def Calculate_cos(x):
    x=x%(2*math.pi)
    result = 0;
    for i in range(10):
        term = (-1)**i*x**(2*i)/factorial(2*i)
        result += term
    return result
    
def Calculate_tan(x):
    sin_result = Calculate_sin(x)
    cos_result = Calculate_cos(x)
    return sin_result / cos_result   
    

