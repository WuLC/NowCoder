# -*- coding: utf-8 -*-
# Created on Mon Mar 12 2018 10:2:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(1) space
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, nums, duplication):
        for i in xrange(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    duplication[0] = nums[i]
                    return True
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
        return False