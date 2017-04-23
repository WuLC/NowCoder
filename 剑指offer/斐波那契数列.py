# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 15:47:37
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 15:49:35
# @Email: liangchaowu5@gmail.com


# 递推法, 时间复杂度O(n)
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in xrange(n-1):
            a, b = b, a+b
        return b 



# 时间复杂度O(logn)
