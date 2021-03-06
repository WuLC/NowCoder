# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-22 00:04:56
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-22 00:05:46
# @Email: liangchaowu5@gmail.com

"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0:
            return False
        m, n = len(array), len(array[0])
        row, col = 0, n-1
        while row < m and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False