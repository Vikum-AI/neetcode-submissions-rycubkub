class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col, 0))

        while q:
            r, c, d = q.popleft()

            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or grid[r][c] == -1
                or (grid[r][c] < 2147483647 and grid[r][c] > 0)):
                continue

            if grid[r][c] == 2147483647:
                grid[r][c] = d

            d += 1

            q.append((r + 1, c, d))
            q.append((r, c + 1, d))
            q.append((r - 1, c, d))
            q.append((r, c - 1, d))






            