# -*- coding: utf-8 -*-
# Created on Mon Mar 19 2018 17:40:13
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# dp, pay attention that '*' in pattern corrresponds to 3 cases
class Solution:
    def match(self, s, pattern):
        m, n = len(pattern), len(s)
        dp = [[False for j in xrange(n+1)] for i in xrange(m+1)]
        dp[0][0] = True
        for i in xrange(1, m+1):
            for j in xrange(n+1):
                if j==0:
                    if pattern[i-1] == '*' and i-2 >= 0:
                        dp[i][j] = dp[i-2][j]
                elif pattern[i-1] == s[j-1] or pattern[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[i-1] == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or ((pattern[i-2] == s[j-1] or pattern[i-2] == '.') and dp[i][j-1])
        return dp[m][n]