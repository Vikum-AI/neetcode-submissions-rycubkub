class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return


            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])

            cur.pop()

            count = 1
            while i+count < len(candidates) and candidates[i] == candidates[i+count]:
                count += 1
            
            dfs(i+count, cur, total)

        dfs(0, [], 0)

        return res



