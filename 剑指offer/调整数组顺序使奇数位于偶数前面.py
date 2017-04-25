# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-25 20:56:28
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-25 21:01:38
# @Email: liangchaowu5@gmail.com


"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

# O(n^2) time, O(1) space
class Solution:
    def reOrderArray(self, array):
        for i in reversed(xrange(len(array))):
            if (array[i]&1) == 0:
                idx = i+1
                while idx < len(array) and (array[idx] & 1):
                    array[idx-1], array[idx] = array[idx], array[idx-1]
                    idx += 1
        return array


# O(n) time, O(n) space
class Solution:
    def reOrderArray(self, array):
        odd = filter(lambda x: (x&1) == 1, array)
        even = filter(lambda x: (x&1) == 0, array)
        return odd+even
        """
        odd, even = [], []
        for i in xrange(len(array)):
            if (array[i]&1) == 1:
                odd.append(array[i])
            else:
                even.append(array[i])
        return  odd+even
        """