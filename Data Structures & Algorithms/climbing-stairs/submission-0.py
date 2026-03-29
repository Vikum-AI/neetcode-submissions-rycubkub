"""
n = 4
1 + 1 + 1 + 1
2 + 2

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)