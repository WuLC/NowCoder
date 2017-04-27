# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-27 20:51:30
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-27 20:52:03
# @Email: liangchaowu5@gmail.com


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