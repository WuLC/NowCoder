1# -*- coding: utf-8 -*-
# Created on Mon Feb 26 2018 20:18:1
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
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        if root.val == expectNumber and root.left == None and root.right == None:
            return[[root.val]]
        tmp = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for path in left:
            tmp.append([root.val] + path)
        for path in right:
            tmp.append([root.val] + path)
        return tmp