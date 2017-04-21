# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-22 00:07:55
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-22 00:08:14
# @Email: liangchaowu5@gmail.com


"""
输入一个链表，从尾到头打印链表每个节点的值。
"""

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        curr = listNode
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        return stack[::-1]