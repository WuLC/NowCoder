# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-26 19:44:52
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-26 19:45:49
# @Email: liangchaowu5@gmail.com

"""
输入一个链表，反转链表后，输出链表的所有元素。
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 三指针，首元素的next必须设为None，否则死循环
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None:
            return pHead
        p1, p2 = pHead, pHead.next
        p1.next = None # must set this, otherwise infinite loop will appear
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1