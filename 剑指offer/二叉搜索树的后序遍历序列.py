# -*- coding: utf-8 -*-
# Created on Mon Feb 26 2018 17:7:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 递归，注意空树不符合要求
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return self.isLegal(sequence)
    
    def isLegal(self, seq):
        if len(seq) == 0:
            return True
        root = seq[-1]
        idx = 0
        while idx < len(seq) - 1 and root > seq[idx]:
            idx += 1
        for i in xrange(idx, len(seq) - 1):
            if seq[i] < root:
                return False
        return self.isLegal(seq[:idx]) and self.isLegal(seq[idx:-1])