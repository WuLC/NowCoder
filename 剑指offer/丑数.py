# -*- coding: utf-8 -*-
# Created on Tue Mar 06 2018 9:11:37
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# merge k sorted list, k is the number of primes
class Solution:
    def GetUglyNumber_Solution(self, n):
        if n==0:
            return 0
        nums = [1]
        idx = [0, 0, 0]
        while len(nums) < n:
            curr = min([nums[idx[0]]*2, nums[idx[1]]*3, nums[idx[2]]*5])
            nums.append(curr)
            if nums[idx[0]]*2 == curr:
                idx[0] += 1
            if nums[idx[1]]*3 == curr:
                idx[1] += 1
            if nums[idx[2]]*5 == curr:
                idx[2] += 1
        return nums[-1]