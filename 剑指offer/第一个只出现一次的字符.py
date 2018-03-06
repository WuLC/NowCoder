# -*- coding: utf-8 -*-
# Created on Tue Mar 06 2018 10:5:47
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# hashmap
from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        count = Counter(s)
        for i in xrange(len(s)):
            if count[s[i]] == 1:
                return i
        return -1