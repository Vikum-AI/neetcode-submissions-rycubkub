class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_sum=0, subset=[]):
            print(cur_sum, target)
            if i >= len(nums) or cur_sum > target:
                return

            if cur_sum == target:
                res.append(subset.copy())
                return 

            dfs(i+1, cur_sum, subset.copy())

            s = subset.copy()
            s.append(nums[i])
            dfs(i, cur_sum+nums[i], s.copy())


        dfs(0)
        return res