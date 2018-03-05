# -*- coding: utf-8 -*-
# Created on Mon Mar 05 2018 20:54:40
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        result = None
        pre, curr = 0, 0
        for num in array:
            pre = curr
            curr = max(num, num+pre)
            result = curr if result == None else max(result, curr)
        return result
                