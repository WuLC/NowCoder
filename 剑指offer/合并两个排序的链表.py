# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-26 19:50:12
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-26 19:51:07
# @Email: liangchaowu5@gmail.com


"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""



# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 设虚拟头结点
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        dummy = ListNode(0)
        curr = dummy
        p1, p2 = pHead1, pHead2
        while p1 and p2:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
            else:
                curr.next = p1
                p1 = p1.next
            curr = curr.next
        if p1:
            curr.next = p1
        elif p2:
            curr.next = p2
        return dummy.next     