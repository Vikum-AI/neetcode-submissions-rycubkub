class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(n, memo={}):
            if n >= len(nums):
                return 0

            if n in memo:
                return memo[n]

            res = max(nums[n] + dfs(n+2), dfs(n+1))
            memo[n] = res

            return res

        return dfs(0)


# O(n^2)


