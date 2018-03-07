# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 21:25:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left, right = 0, len(array) - 1
        while left < right:
            curr_sum = array[left]+array[right]
            if curr_sum == tsum:
                return [array[left], array[right]]
            elif curr_sum > tsum:
                right -= 1
            else:
                left += 1
        return []