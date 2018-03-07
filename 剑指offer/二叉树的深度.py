# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 20:7:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# divide and conquer
class Solution:
    def TreeDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return 1 + max(self.TreeDepth(root.left), self.TreeDepth(root.right))