# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 21:3:13
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bottom up solution
class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.isBalance(pRoot) != -1
    
    def isBalance(self, root):
        """return max depth if balanced else -1"""
        if root == None:
            return 0
        leftDepth = self.isBalance(root.left)
        rightDepth = self.isBalance(root.right)
        if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth)>1:
            return -1
        return 1 + max(leftDepth, rightDepth)