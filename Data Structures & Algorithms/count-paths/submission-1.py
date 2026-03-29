class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(r, c, memo={}):
            if (r >= m or c >= n
                or r < 0 or c < 0):
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]

            if r == m - 1 and c == n - 1:
                return 1

            res = dfs(r + 1, c) + dfs(r, c + 1)

            memo[(r, c)] = res

            return res


        return dfs(0, 0)