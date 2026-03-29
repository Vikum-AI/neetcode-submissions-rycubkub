from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visit = set()

        def dfs(r, c, i):
            if (r >= ROWS or c >= COLS
                or r < 0 or c < 0
                or i > len(word)
                or (r, c) in visit
                or board[r][c] != word[i]):
                return False

            if i == len(word) - 1:
                return True

            visit.add((r, c))
                    
            res = (dfs(r + 1, c, i+1) or
                dfs(r - 1, c, i+1) or
                dfs(r, c + 1, i+1) or
                dfs(r, c - 1, i+1))

            visit.remove((r, c))

            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False



