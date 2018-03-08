# -*- coding: utf-8 -*-
# Created on Thu Mar 08 2018 22:21:31
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归，也可采用中序遍历
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k <= 0 or pRoot==None:
            return None
        left_count = self.count(pRoot.left)
        if left_count == k-1:
            return pRoot
        elif left_count < k-1:
            return self.KthNode(pRoot.right, k-left_count-1)
        else:
            return self.KthNode(pRoot.left, k)

    def count(self, root):
        if root == None:
            return 0
        else:
            return 1+self.count(root.left)+self.count(root.right)