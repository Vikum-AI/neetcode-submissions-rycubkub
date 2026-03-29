"""
n = 4
1 + 1 + 1 + 1
2 + 2

"""

from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [1, 2]

        for i in range(2, n):
            memo.append(memo[i - 1] + memo[i - 2])

        return memo[n - 1]


