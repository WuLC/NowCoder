# -*- coding: utf-8 -*-
# Created on Mon Mar 12 2018 22:48:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) space
class Solution:
    def EntryNodeOfLoop(self, pHead):
        visited = set()
        curr = pHead
        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next


# O(1) space
