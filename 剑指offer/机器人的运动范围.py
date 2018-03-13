# -*- coding: utf-8 -*-
# Created on Tue Mar 13 2018 18:19:54
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# bfs or dfs
from collections import deque
class Solution:
    def movingCount(self, threshold, rows, cols):
        # bfs
        if threshold<0 or rows<=0 or cols<=0:
            return 0
        visited = [[0 for j in xrange(cols)] for i in xrange(rows)]
        visited[0][0] = 1
        queue = deque([(0, 0)])
        count = 0
        direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while len(queue) > 0:
            curr = queue.popleft()
            count += 1
            for d in direct:
                r, c = curr[0]+d[0], curr[1]+d[1]
                if 0 <= r < rows and 0 <= c < cols and visited[r][c]==0 and sum([int(c) for c in str(r)+str(c)]) <= threshold:
                    visited[r][c] = 1
                    queue.append((r, c))
        return count