# -*- coding: utf-8 -*-
# Created on Tue Mar 13 2018 10:11:59
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers, elegant code
class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        dummy = ListNode(0)
        curr = dummy
        p1, p2 = pHead, pHead.next
        while p2:
            if p1.val != p2.val:
                if p1.next == p2:
                    curr.next = p1
                    curr = curr.next
                p1 = p2
            p2=p2.next
        curr.next = p1 if p1.next == None else None # last node is valid
        return dummy.next