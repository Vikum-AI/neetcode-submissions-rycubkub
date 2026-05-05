class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))

            while queue:
                r, c = queue.popleft()
                
                if (r < 0 or r >= ROWS
                    or c < 0 or c >= COLS
                    or (r, c) in visit
                    or grid[r][c] != "1"):
                    continue

                visit.add((r, c))

                queue.append((r + 1, c))
                queue.append((r, c + 1))
                queue.append((r - 1, c))
                queue.append((r, c - 1))

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
               if grid[r][c] == "1" and (r, c) not in visit:
                res += 1
                bfs(r, c)

        return res 




