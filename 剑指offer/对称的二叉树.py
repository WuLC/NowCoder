# -*- coding: utf-8 -*-
# Created on Fri Mar 09 2018 14:48:11
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# divide and conquer
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
        return self.symmetry(pRoot.left, pRoot.right)
    
    
    def symmetry(self, r1, r2):
        if r1==None and r2==None:
            return True
        elif r1==None or r2==None:
            return False
        else:
            return r1.val==r2.val and self.symmetry(r1.left, r2.right) and self.symmetry(r1.right, r2.left)
        
    
    