# -*- coding: utf-8 -*-
# Created on Thu Mar 15 2018 10:8:10
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, O(n) space
class Solution:
    def multiply(self, A):
        n = len(A)
        left, right = [1], [1]
        
        curr = 1
        for i in xrange(n-1):
            curr *= A[i]
            left.append(curr)
        curr = 1
        for i in reversed(xrange(1, n)):
            curr *= A[i]
            right.append(curr)
        
        result = []
        for i in xrange(n):
            result.append(left[i]*right[n-i-1])
        return result