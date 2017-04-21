# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-22 00:06:41
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-22 00:07:35
# @Email: liangchaowu5@gmail.com


"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        result = ''
        for char in s:
            result += '%20' if char == ' ' else char
        return result