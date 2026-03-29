class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, curMax=None, memo={}):
            if i >= len(nums):
                return 0

            if (i, curMax) in memo:
                return memo[(i, curMax)]

            if curMax is None:
                res = max(1 + dfs(i+1, nums[i], memo), dfs(i+1, None, memo))

            elif nums[i] > curMax:
                res = max(1 + dfs(i+1, nums[i], memo), dfs(i+1, curMax, memo))

            else:
                res = (dfs(i+1, curMax, memo))

            memo[(i, curMax)] = res

            return res 


        return dfs(0)

