# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-04-25 18:55:50
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-25 18:56:06
# @Email: liangchaowu5@gmail.com

# similar to binary search
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
        