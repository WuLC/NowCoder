# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 21:34:1
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution, pay attention to empty string
class Solution:
    def ReverseSentence(self, s):
        if len(s.strip()) == 0:
            return s
        return ' '.join(s.split()[::-1])