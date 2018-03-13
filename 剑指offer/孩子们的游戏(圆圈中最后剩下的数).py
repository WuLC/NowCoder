# -*- coding: utf-8 -*-
# Created on Tue Mar 13 2018 11:17:39
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 约瑟夫问题

# cycled linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n <= 0 or m <= 0:
            return -1
        if m == 1:
            return n-1
        # build the cycle
        head = ListNode(0)
        curr = head
        for i in xrange(1, n):
            curr.next = ListNode(i)
            curr = curr.next
        curr.next = head
        curr = head
        
        # repeat the process
        count = n
        while count > 1:
            for i in xrange(m-2):
                curr = curr.next
            curr.next = curr.next.next
            curr = curr.next
            count -= 1
        return curr.val