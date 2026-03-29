class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(i, total=0, memo={}):
            if i >= len(coins) or total > amount:
                return 0

            if total == amount:
                return 1

            if (i, total) in memo:
                return memo[(i, total)]

            count = dfs(i, total+coins[i], memo) + dfs(i+1, total, memo)
            memo[(i, total)] = count

            return count

        return dfs(0)