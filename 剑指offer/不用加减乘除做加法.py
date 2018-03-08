# -*- coding: utf-8 -*-
# Created on Thu Mar 08 2018 20:47:51
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bit manipulation
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            tmp = num1^num2
            carry = (num1&num2)<<1
            num1, num2 = tmp, carry
        return num1