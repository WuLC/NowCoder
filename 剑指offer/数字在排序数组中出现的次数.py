# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 20:2:52
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# binary search
class Solution:
    def GetNumberOfK(self, data, k):
        return self.helper(data, 0, len(data)-1, k)
    
    def helper(self, data, left, right, k):
        if left > right:
            return 0
        elif left==right:
            return 1 if data[left] == k else 0
        mid = left + ((right-left)>>1)
        if data[mid] > k:
            return self.helper(data, left, mid-1, k)
        elif data[mid] < k:
            return self.helper(data, mid+1, right, k)
        else:
            return 1 + self.helper(data, left, mid-1, k) + self.helper(data, mid+1, right, k)