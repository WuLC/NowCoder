# -*- coding: utf-8 -*-
# Created on Mon Feb 26 2018 20:51:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# divide and conquer
class Solution:
    def Convert(self, root):
        # write code here
        if root == None:
            return None
        leftHead = self.Convert(root.left)
        rightHead = self.Convert(root.right)
        # left tree
        if leftHead == None:
            root.left = None
        else:
            curr = leftHead
            while curr.right:
                curr = curr.right
            root.left = curr
            curr.right = root
        # right tree
        if rightHead == None:
            root.right = None
        else:
            root.right = rightHead
            rightHead.left = root
        return root if leftHead == None else leftHead
        