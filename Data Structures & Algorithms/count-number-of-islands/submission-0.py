class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        res = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                if (row, col) in visit:
                    continue

                if row >= ROWS or col >= COLS:
                    continue

                if row < 0 or col < 0:
                    continue

                if grid[row][col] == "1":
                    visit.add((row, col))

                    queue.append((row + 1, col))
                    queue.append((row, col + 1))
                    queue.append((row - 1, col))
                    queue.append((row, col - 1))

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    res += 1


        return res

                
        