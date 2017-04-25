# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-04-25 18:55:50
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-25 20:21:12
# @Email: liangchaowu5@gmail.com


"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""

# 类二分查找
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        negative = True if exponent < 0 else False
        exponent = abs(exponent)
        result,count = base, 1
        while count <= (exponent >> 1):
            result *= result
            count *= 2
        result *= self.Power(base, exponent-count)
        return 1/result if negative else result


# 参考原书答案
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        negative = True if exponent < 0 else False
        exponent = abs(exponent)
        result = self.Power(base, exponent >> 1)
        result *= result
        if (exponent&1):
            result *= base
        return 1/result if negative else result