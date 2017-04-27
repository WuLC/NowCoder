# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-27 20:30:45
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-27 20:33:16
# @Email: liangchaowu5@gmail.com


"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursive, but the code is redundant
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val == pRoot2.val:
            if pRoot2.left == None and pRoot2.right == None:
                return True
            elif pRoot2.left == None:
                return self.HasSubtree(pRoot1.right, pRoot2.right) or 
                       self.HasSubtree(pRoot1.left, pRoot2) or 
                       self.HasSubtree(pRoot1.right, pRoot2)
            elif pRoot2.right == None:
                return self.HasSubtree(pRoot1.left, pRoot2.left) or 
                       self.HasSubtree(pRoot1.left, pRoot2) or 
                       self.HasSubtree(pRoot1.right, pRoot2)
            else:
                return self.HasSubtree(pRoot1.right, pRoot2.right) and self.HasSubtree(pRoot1.left, pRoot2.left) or 
                       self.HasSubtree(pRoot1.right, pRoot2) or 
                       self.HasSubtree(pRoot1.left, pRoot2)
        else:
            return self.HasSubtree(pRoot1.right, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2)