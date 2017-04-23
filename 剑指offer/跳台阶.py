# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 16:32:48
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 16:34:17
# @Email: liangchaowu5@gmail.com

# dp, time complexity: O(n)
# similar to Fibonaci Array
class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        a, b = 1, 2
        for _ in xrange(number-2):
            a, b = b, a+b
        return b