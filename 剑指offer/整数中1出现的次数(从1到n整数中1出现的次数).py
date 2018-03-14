# -*- coding: utf-8 -*-
# Created on Wed Mar 14 2018 17:20:22
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# count the number of 1 for each bit
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        s = str(n)
        for i in range(len(s)):
            high = int(s[:i]) if i != 0 else 0
            low = int(s[i+1:]) if i != len(s)-1 else 0
            if s[i] == '0':
                count += high*(10**(len(s)-i-1))
            elif s[i] == '1':
                count += high*(10**(len(s)-i-1)) + low + 1
            else:
                count += (high+1) * (10**(len(s)-i-1))
        return count