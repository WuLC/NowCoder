# -*- coding: utf-8 -*-
# Created on Tue Mar 13 2018 22:32:2
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap
from collections import Counter
class Solution:
    def IsContinuous(self, nums):
        if len(nums) != 5:
            return False
        count = Counter(nums)
        min_num, max_num = 14, -1
        for k in count.keys():
            if k == 0:
                continue
            if count[k] > 1:
                return False
            min_num = min(min_num, k)
            max_num = max(max_num, k)
        return max_num-min_num <= 4