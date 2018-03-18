# -*- coding: utf-8 -*-
# Created on Thu Mar 15 2018 10:27:42
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# traverse level by level
class Solution:
    def Print(self, pRoot):
        if pRoot == None:
            return []
        flag = 1
        result = []
        curr = [pRoot]
        while curr:
            next = []
            for node in curr:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if flag==1:
                result.append([node.val for node in curr])
            else:
                result.append([curr[i].val for i in reversed(xrange(len(curr)))])
            flag *= -1
            curr = next
        return result