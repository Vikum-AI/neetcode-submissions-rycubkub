class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            if (r >= ROWS or c >= COLS
                or r < 0 or c < 0
                or (r, c) in seen
                or grid[r][c] != "1"):
                    return
            
            seen.add((r, c))

            bfs(r + 1, c)
            bfs(r, c + 1)
            bfs(r - 1, c)
            bfs(r, c - 1)



        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in seen:
                    res += 1
                    bfs(row, col)

        return res