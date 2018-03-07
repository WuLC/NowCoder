# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 19:52:43
# Author: WuLC
# EMail: liangchaowu5@gmail.com


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# change head to the other list when metting tail
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        h1, h2 = pHead1, pHead2
        while h1 or h2:
            if h1 == None:
                h1 = pHead2
            if h2 == None:
                h2 = pHead1
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
            