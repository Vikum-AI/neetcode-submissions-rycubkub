"""
n = 4
1 + 1 + 1 + 1
2 + 2

"""

from collections import defaultdict

class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n in memo:
            return memo[n]

        result = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        memo[n] = result

        return result
