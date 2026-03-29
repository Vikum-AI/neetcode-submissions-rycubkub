

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, cur_sum=0):
            if cur_sum == target:
                res.append(comb.copy())
                return 

            if cur_sum > target:
                return 

            if i >= len(nums):
                return 

            comb.append(nums[i])
            dfs(i, comb, cur_sum+nums[i])

            comb.pop()
            dfs(i+1, comb, cur_sum)


        dfs(0, [], 0)

        return res
