# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-04 11:16:39
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-04 11:21:03
# @Email: liangchaowu5@gmail.com

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
"""


# 用两个栈，一个存储所有元素，另外一个栈顶存储当前最小元素
class Solution:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, node):
        self.stack.append(node)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= node:
            self.min_stack.append(node)
        
    
    def pop(self):
        if self.stack:
            tmp = self.stack.pop()
            if tmp == self.min_stack[-1]:
                self.min_stack.pop()
            return tmp
        else:
            return None 
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def min(self):
        return self.min_stack[-1] if self.min_stack else None