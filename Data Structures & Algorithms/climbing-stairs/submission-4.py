class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        p1, p2 = 1, 2
        count = 0

        for i in range(3, n+1):
            count = p1 + p2
            p1 = p2
            p2 = count

        return count
            
