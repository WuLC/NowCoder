# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-23 16:59:16
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-23 17:00:08
# @Email: liangchaowu5@gmail.com


# 数学归纳法，2^(n-1)
class Solution:
    def jumpFloorII(self, number):
        return pow(2, number-1)