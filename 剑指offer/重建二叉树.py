# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-22 00:28:13
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-22 00:29:49
# @Email: liangchaowu5@gmail.com


"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归，注意所有数字不重复，若重复则无法构建   
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0 or len(tin) == 0:
            return None
        root = TreeNode(pre[0])
        left_nodes = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:left_nodes+1], tin[:left_nodes])
        root.right = self.reConstructBinaryTree(pre[left_nodes+1:], tin[left_nodes:])
        return root