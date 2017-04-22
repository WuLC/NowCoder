# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-22 10:36:53
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-22 11:05:58
# @Email: liangchaowu5@gmail.com

# 二分查找，注意数组是非递减数组，也就是可能含有重复元素
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        result = 0
        left, right = 0, len(rotateArray)-1
        while left <= right:
            mid = left + ((right-left)>>1)
            if rotateArray[mid] <= rotateArray[right]:
                right = mid - 1
            elif rotateArray[mid] >= rotateArray[left]:
                left = mid + 1
            result = rotateArray[mid] if result == 0 else min(result, rotateArray[mid])
        return result