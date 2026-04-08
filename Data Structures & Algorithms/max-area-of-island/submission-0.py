class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(ro, co):
            q = deque()
            q.append((ro, co))

            area = 0

            while q:
                r, c = q.popleft()

                if (r < 0 or c < 0
                    or r >= ROWS or c >= COLS
                    or grid[r][c] != 1
                    or (r, c) in visit):
                    continue

                area += 1
                visit.add((r, c))
                
                q.append((r + 1, c))
                q.append((r, c + 1))
                q.append((r - 1, c))
                q.append((r, c - 1))

            return area

        max_area = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visit:
                    area = bfs(row, col)
                    max_area = max(max_area, area)

        return max_area