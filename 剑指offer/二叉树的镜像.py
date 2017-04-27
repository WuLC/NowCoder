# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-27 20:51:30
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-27 20:53:46
# @Email: liangchaowu5@gmail.com


"""
操作给定的二叉树，将其变换为源二叉树的镜像。 
输入描述:
二叉树的镜像定义：源二叉树 
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return root
        left = self.Mirror(root.right)
        right = self.Mirror(root.left)
        root.left, root.right = left, right
        return root