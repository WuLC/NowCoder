# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 21:20:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two pointers
class Solution:
    def FindContinuousSequence(self, tsum):
        result = []
        left, right = 1, 2
        curr_sum = 1
        while right <= tsum+1:
            if curr_sum == tsum:
                if left + 1 < right:
                    result.append(range(left, right))
                curr_sum -= left
                left += 1
            elif curr_sum < tsum:
                curr_sum += right
                right += 1
            else:
                curr_sum -= left
                left += 1
        return result