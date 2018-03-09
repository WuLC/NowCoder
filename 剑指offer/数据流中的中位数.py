# -*- coding: utf-8 -*-
# Created on Fri Mar 09 2018 10:57:14
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# two heaps
# max heap for small half numbers and min heap for large half numbers
from heapq import *
class Solution:
    def __init__(self):
        self.large, self.small = [], []
        
    def Insert(self, num):
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.small) > len(self.large):
            heappush(self.large, -heappop(self.small))
        
    def GetMedian(self):
        if len(self.large)!= len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0])/2.0