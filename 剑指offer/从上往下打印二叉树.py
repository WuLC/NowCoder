# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-06 10:54:38
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-06 10:55:17
# @Email: liangchaowu5@gmail.com


"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        

# 逐层遍历二叉树
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root == None:
            return []
        result = []
        curr, next = [root], []
        while len(curr) > 0:
            for node in curr:
                result.append(node.val)
                if node.left != None:
                    next.append(node.left)
                if node.right != None:
                    next.append(node.right)
            curr = next
            next = []
        return result            