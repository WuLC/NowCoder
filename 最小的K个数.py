# -*- coding: utf-8 -*-
# Created on Sun Mar 04 2018 17:34:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# heap
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        tmp = []
        for num in tinput:
            heapq.heappush(tmp, -num)
            if len(tmp) > k:
                heapq.heappop(tmp)
        result = []
        while len(tmp) > 0:
            result.append(-1*heapq.heappop(tmp))
        return result[::-1]
            
        