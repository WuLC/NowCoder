# -*- coding: utf-8 -*-
# Created on Fri Mar 09 2018 22:49:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# traverse by level
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        result = []
        if root==None:
            return result
        curr = [root]
        while curr:
            next = []
            for node in curr:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            result.append([node.val for node in curr])
            curr = next
        return result
        