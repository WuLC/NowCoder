# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 15:47:37
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 19:36:45
# @Email: liangchaowu5@gmail.com

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
注：斐波那契数列从0开始
"""

# 递推法, 时间复杂度O(n)；避免用递归
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in xrange(n-1):
            a, b = b, a+b
        return b 