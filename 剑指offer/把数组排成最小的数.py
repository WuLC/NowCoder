# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 9:53:12
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# 自定义排序函数
class Solution:
    def PrintMinNumber(self, numbers):
        def compare(n1, n2):
            if n1+n2 < n2+n1:
                return -1
            elif n1+n2 == n2+n1:
                return 0
            else:
                return 1
        s_nums = [str(num) for num in numbers]
        return ''.join(sorted(s_nums, cmp = compare))