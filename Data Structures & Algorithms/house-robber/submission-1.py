class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(n, memo={}):
            if n in memo:
                return memo[n]

            if n >= len(nums):
                return 0

            result = max(nums[n] + dfs(n + 2, memo), dfs(n + 1, memo))
            memo[n] = result

            return result
            
        return dfs(0)
