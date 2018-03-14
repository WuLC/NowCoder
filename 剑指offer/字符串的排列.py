# -*- coding: utf-8 -*-
# Created on Wed Mar 14 2018 22:58:20
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# divide and conquer
class Solution:
    def Permutation(self, ss):
        ss = sorted(ss)
        return self.helper(ss)

    def helper(self, ss):
        result = []
        if len(ss) == 1:
            result.append(ss[0])
        else:
            for i in range(len(ss)):
                if i > 0 and ss[i] == ss[i-1]:
                    continue
                else:
                    for left in self.helper(ss[:i]+ss[i+1:]):
                        result.append(ss[i]+left)
        return result