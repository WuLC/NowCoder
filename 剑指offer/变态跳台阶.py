# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 16:59:16
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 19:34:45
# @Email: liangchaowu5@gmail.com

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


# 举例子，数学归纳法，2^(n-1)
class Solution:
    def jumpFloorII(self, number):
        return pow(2, number-1)