# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 19:40:23
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-25 19:50:14
# @Email: liangchaowu5@gmail.com


"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

# bit manipulation
# 注意负数右移时候最高位会一直保持为1，因此不能用 while(n) 的循环方式
class Solution:
    def NumberOf1(self, n):
        result = 0
        for _ in xrange(32):
            result += (1&n)
            n >>= 1
        return result
