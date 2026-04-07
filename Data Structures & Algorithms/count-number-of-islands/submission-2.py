class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()

        def bfs(r, c):
            print('bfs called')
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()

                if (row >= ROWS or col >= COLS 
                    or row < 0 or col < 0 
                    or grid[row][col] == '0'
                    or (row, col) in visit):
                    continue
                
                visit.add((row, col))

                q.append((row + 1, col))
                q.append((row, col + 1))
                q.append((row - 1, col))
                q.append((row, col - 1))

        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                print(r, c)
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    res += 1

        return res