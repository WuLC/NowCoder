# -*- coding: utf-8 -*-
# Created on Mon Feb 26 2018 15:43:36
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 递归，注意只有一行或一列的情况
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        return self.helper(matrix, 0, 0, n-1, m-1)
        
    def helper(self, matrix, left, top, right, bottom):
        tmp = []
        if left > right or top > bottom:
            return tmp
        for i in xrange(left, right+1):
            tmp.append(matrix[top][i])
        for i in xrange(top+1, bottom+1):
            tmp.append(matrix[i][right])
        if top != bottom:
            for i in xrange(right-1, left-1, -1):
                tmp.append(matrix[bottom][i])
        if left != right:
            for i in xrange(bottom-1, top, -1):
                tmp.append(matrix[i][left])
        return tmp + self.helper(matrix, left+1, top+1, right-1, bottom-1)