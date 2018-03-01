# -*- coding: utf-8 -*-
# Created on Thu Mar 01 2018 21:2:7
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, O(n) space
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = {}
        num, curr_max = None, 0
        for number in numbers:
            count.setdefault(number, 0)
            count[number] += 1
            if count[number] > curr_max:
                num, curr_max = number, count[number]
        return num if curr_max > len(numbers)/2 else 0
        
                
        
        