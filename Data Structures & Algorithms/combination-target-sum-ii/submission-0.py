class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, comb):
            if cur == target:
                res.append(comb.copy())
                return

            if (i >= len(candidates) 
                or cur > target):
                return

            comb.append(candidates[i])
            dfs(i+1, cur+candidates[i], comb)
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, cur, comb)


        dfs(0, 0, [])

        return res