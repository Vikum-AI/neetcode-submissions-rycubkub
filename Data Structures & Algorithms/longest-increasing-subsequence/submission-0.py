class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, curMax=None):
            if i >= len(nums):
                return 0

            if curMax is None:
                res = max(1 + dfs(i+1, nums[i]), dfs(i+1, None))

            elif nums[i] > curMax:
                res = max(1 + dfs(i+1, nums[i]), dfs(i+1, curMax))

            else:
                res = (dfs(i+1, curMax))

            return res 


        return dfs(0)

