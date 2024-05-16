##函数功能##
#实现arctan函数
#输入 x ：需要计算的反三函数值   
#输出 result_rad ：返回弧度制角度    (-pi/2,pi/2)
#    result_deg: 返回角度 

import math

def Calculate_arctan(x):
    
    result_rad=0
    for i in range(1,100):
        term = (-1)**(i+1)*x**(2*i-1)/(2*i-1)
        result_rad += term

    #result_deg = result_rad*180/math.pi    
    
    return result_rad
#if __name__ == "__main__":
    #x = 0.9
    #result_rad,result_deg = Calculate_arctan(x)
    #print(result_rad,result_deg)

