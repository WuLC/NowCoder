# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 19:32:26
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 19:33:32
# @Email: liangchaowu5@gmail.com


"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


# dp, similar to Fibonaci Array
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        a, b = 1, 2
        for _ in xrange(number - 2):
            a, b = b, a+b
        return b