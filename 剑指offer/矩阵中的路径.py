# -*- coding: utf-8 -*-
# Created on Wed Mar 14 2018 11:28:49
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# backtrack with dfs
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(path) == 0:
            return True
        if rows <= 0 or cols <= 0:
            return False
        self.visited = [0 for _ in xrange(rows*cols)]
        for i in xrange(rows):
            for j in xrange(cols):
                if self.dfs(matrix, i, j, rows, cols, path):
                    return True
        return False
                
    
    def dfs(self, matrix, i, j, rows, cols, path):
        if len(path) == 0:
            return True
        idx = i*cols + j
        if i<0 or i>=rows or j<0 or j>=cols or self.visited[idx] == 1 or matrix[idx] != path[0]:
            return False
        self.visited[idx] = 1
        direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for d in direct:
            if self.dfs(matrix, i+d[0], j+d[1], rows, cols, path[1:]):
                return True
        self.visited[idx] = 0
        return False