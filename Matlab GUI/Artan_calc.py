##函数功能##
#实现arctan函数
#输入 x ：需要计算的反三函数值   
#输出 result_rad ：返回弧度制角度    (-pi/2,pi/2)
#    result_deg: 返回角度 

import Arcsin_calc 
import math
def Calculate_arctan(x):
    
    result_rad=0
    deta = x/math.sqrt(1+x*x)
    result_rad,a = Arcsin_calc.Arcsin_calc(deta)

    result_deg = result_rad*180/math.pi    
    
    return result_rad,result_deg
if __name__ == "__main__":
    x = math.sqrt(3)
    result_rad,result_deg = Calculate_arctan(x)
    print(result_rad,result_deg)
