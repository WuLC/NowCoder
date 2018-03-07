# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 21:27:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# one line solution
class Solution:
    def LeftRotateString(self, s, n):
        return s[n:]+s[:n]