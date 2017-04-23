# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 16:32:48
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 19:35:26
# @Email: liangchaowu5@gmail.com



"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

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