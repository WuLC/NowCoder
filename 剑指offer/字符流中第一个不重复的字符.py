# -*- coding: utf-8 -*-
# Created on Sat Mar 10 2018 9:10:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 可在插入任意时刻找到第一个只出现一次的字符
from collections import deque, defaultdict
class Solution:
    def __init__(self):
        self.queue = deque()
        self.count = defaultdict(int)
        
    def FirstAppearingOnce(self):
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else '#'
        
    def Insert(self, char):
        self.count[char] += 1
        if self.count[char] == 1:
            self.queue.append(char)