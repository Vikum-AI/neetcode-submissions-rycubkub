class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        def dfs(i, memo={}):
            if i == n:
                return 1

            if i > n:
                return 0

            if i in memo:
                return memo[i]

            res = dfs(i+1, memo) + dfs(i+2, memo)

            memo[i] = res

            return res

        return dfs(0)
