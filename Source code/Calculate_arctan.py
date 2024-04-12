##函数功能##
#实现arctan函数
#输入 x ：需要计算的反三函数值   
#输出 result_rad ：返回弧度制角度    (-pi/2,pi/2)
#    result_deg: 返回角度 

import math
def Calculate_arctan(x):
    n=100000
    result_rad = 0
    sign = 1
    power = x
    for i in range(1,n+1):
        term = power/(2*i-1)
        result_rad += sign *term
        power *= x**2
        sign *= -1

    result_deg = result_rad*180/math.pi    
    return result_rad,result_deg
if __name__ == "__main__":
    x = 0.9
    result_rad,result_deg = Calculate_arctan(x)
    print(result_rad,result_deg)

