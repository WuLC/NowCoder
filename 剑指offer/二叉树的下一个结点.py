# -*- coding: utf-8 -*-
# Created on Mon Mar 12 2018 9:38:56
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# 利用父指针
class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return None
        elif pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:
            while pNode.next and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode.next if pNode.next else None