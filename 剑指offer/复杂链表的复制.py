# -*- coding: utf-8 -*-
# Created on Mon Feb 26 2018 20:39:28
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# O(n^2) 时间复杂度
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        head = RandomListNode(pHead.label)
        curr, pCurr = head, pHead.next
        length = 1
        while pCurr:
            curr.next = RandomListNode(pCurr.label)
            curr = curr.next
            pCurr = pCurr.next
            length += 1
        curr, pCurr = head, pHead
        while pCurr:
            pRandom = pCurr.random
            count = 0
            while pRandom:
                count += 1
                pRandom = pRandom.next
            tmp = head
            for _ in xrange(length - count):
                tmp = tmp.next
            curr.random = tmp
            curr = curr.next
            pCurr = pCurr.next
        return head
            