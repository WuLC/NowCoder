# -*- coding: utf-8 -*-
# Created on Sat Mar 10 2018 9:10:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 可在插入任意时刻找到第一个只出现一次的字符
from collections import deque, defaultdict
class Solution:
    def __init__(self):
        self.count = defaultdict()
        self.chars = deque()
        
    def FirstAppearingOnce(self):
        while len(self.chars) > 0 and self.count[self.chars[0]] > 1:
            self.chars.popleft()
        return self.chars[0] if len(self.chars) > 0 else '#'
        
    def Insert(self, char):
        if char not in self.count:
            self.chars.append(char)
            self.count[char] += 1
        else:
            self.count[char] += 1