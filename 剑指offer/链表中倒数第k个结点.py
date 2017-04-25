# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-25 21:07:17
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-25 21:07:43
# @Email: liangchaowu5@gmail.com

"""
输入一个链表，输出该链表中倒数第k个结点。
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# two pointers
class Solution:
    def FindKthToTail(self, head, k):
        p1 = head
        for _ in xrange(k):
            if p1:
                p1 = p1.next
            else:
                return None
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2