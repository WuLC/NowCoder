# -*- coding: utf-8 -*-
# Created on Wed Mar 07 2018 21:52:8
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bit manipulation
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        tmp = 0
        for num in array:
            tmp ^= num
        lowbit = tmp&-tmp
        num1, num2 = 0, 0
        for num in array:
            if (num&lowbit) == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]