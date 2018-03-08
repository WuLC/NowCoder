# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 18:20:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# merge sort
class Solution:
    def InversePairs(self, nums):
        self.count = 0
        self.mergeSort(nums)
        return self.count
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)>>1
        left, right = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:])
        idx1, idx2 = 0, 0
        for i in xrange(len(nums)):
            if idx1 < len(left) and (idx2==len(right) or left[idx1] <= right[idx2]):
                nums[i] = left[idx1]
                self.count += idx2
                idx1 += 1
            else:
                nums[i] = right[idx2]
                idx2 += 1
        return nums
        