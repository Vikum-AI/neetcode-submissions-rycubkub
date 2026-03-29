from collections import defaultdict
from copy import deepcopy

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(new_target, comb=[]):
            if new_target == 0:
                comb.sort()
                if comb in results:
                    return []
                return comb

            if new_target < 0:
                return []

            for num in nums:
                diff = new_target - num
                new_comb = comb.copy()
                new_comb.append(num)

                res = dfs(diff, new_comb)
                
                
                if res:
                    res.sort()
                    results.append(res)

        dfs(target)

        return results