import math
from double_factorial import double_factorial 

def Arcsin_calc(data):
    if data == 1:
        return 1.5707963267,90
    if data == -1:
        return -1.5707963267,-90  
    if data <-1 or data >1:
        return 99,99
    k = 999
    result = 0
    for i in range (1,k+1,2):
        if(i==1):
            result = data
        else:
            deta = (double_factorial(i-2)/double_factorial(i-1))*math.pow(data,i)/i
            result = result+deta
    rad = result
    deg = result*180/math.pi
    return rad,deg


    
