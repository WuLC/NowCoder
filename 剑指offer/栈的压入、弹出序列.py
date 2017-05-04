# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-04 14:21:27
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-04 14:22:58
# @Email: liangchaowu5@gmail.com

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""

# 用一个栈存储当前无法从 pushV中弹出的元素
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False
        idx, stack = 0, []
        for num in popV:
            if stack and stack[-1] == num:
                stack.pop()
            else:
                while idx < len(pushV) and pushV[idx] != num:
                    stack.append(pushV[idx])
                    idx += 1
                if idx < len(pushV) and pushV[idx] == num:
                    idx += 1
        return True if idx == len(pushV) and len(stack) == 0 else False