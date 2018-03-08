# -*- coding: utf-8 -*-
# Created on Thu Mar 08 2018 22:42:20
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# deque, O(n) time complexity
from collections import deque
class Solution:
    def maxInWindows(self, nums, k):
        if k <= 0:
            return []
        result = []
        idx = deque()
        for i in xrange(len(nums)):
            if idx and idx[0] < i-k+1:
                idx.popleft()
            while idx and nums[idx[-1]] < nums[i]:
                idx.pop()
            idx.append(i)
            if i >= k-1:
                result.append(nums[idx[0]])
        return result