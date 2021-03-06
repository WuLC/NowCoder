# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-22 00:36:03
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-22 00:46:42
# @Email: liangchaowu5@gmail.com

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

# 一个栈存放入队元素，一个栈存放出队元素
# 出队栈为空时，从入队栈pop出所有元素存到入队栈中
class Solution:
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
        
    def push(self, node):
        self.in_stack.append(node)
        
        
    def pop(self):
        if self.out_stack:
            return self.out_stack.pop()
        if len(self.in_stack) == 0:
            return None
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()