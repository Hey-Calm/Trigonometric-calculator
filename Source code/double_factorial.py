#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：段睿
# 创建：2024-04-03
# 更新：2024-04-03
# 功能：计算双阶乘，用于计算arcsin

def double_factorial(n):
    if n < 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result

