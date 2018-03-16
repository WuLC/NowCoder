# -*- coding: utf-8 -*-
# Created on Thu Mar 08 2018 20:47:51
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bit manipulation

# Java version works
public class Solution
{
    public int Add(int num1,int num2) 
    {
        int carry;
        while(num2!=0)
        {
            carry = (num1&num2)<<1;
            num1 = num1^num2;
            num2 = carry;
        }
        return num1;
    }
}

# python version do not work cause it will automatically convert int to long
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            tmp = num1^num2
            carry = (num1&num2)<<1
            num1, num2 = tmp, carry
        return num1