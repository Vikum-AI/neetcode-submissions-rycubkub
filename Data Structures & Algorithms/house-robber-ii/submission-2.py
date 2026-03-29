# [2,9,8,3,6]

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 = {}
        memo2 = {}
        def dfs(n, nums_copy, memo):
            if n >= len(nums_copy):
                return 0

            if n in memo:
                return memo[n]

            result = max(nums_copy[n] + dfs(n + 2, nums_copy, memo), dfs(n + 1, nums_copy, memo))

            memo[n] = result

            print(memo, nums_copy)

            return result

        return max(dfs(0, nums[:-1] if len(nums) > 1 else nums, memo1), dfs(1, nums, memo2))