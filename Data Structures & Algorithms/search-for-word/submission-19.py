""" 
["A","B","C","E"]
["S","F","E","S"]
["A","D","E","E"]

word = ABCESEEEFS 
"""



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(r, c, i=0):
            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or board[r][c] != word[i]
                or (r, c) in visit):
                return False
            
            index = i + 1

            if (i >= len(word) - 1):
                return True

            visit.add((r, c))
            
            for direction in directions:
                x, y = direction
                
                if dfs(r + x, c + y, index):
                    return True

            visit.remove((r, c))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    visit = set()
                    if dfs(row, col):
                        return True

        return False