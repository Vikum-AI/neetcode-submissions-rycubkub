class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev=float('inf')):
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS
                or heights[r][c] < prev
                or (r, c) in visit):
                return 

            visit.add((r, c))

            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        
        for r in range(ROWS):
            print('pac1', heights[r][0])
            print('atl1', heights[r][COLS - 1])

            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for c in range(COLS):
            print('pac2', heights[0][c])
            print('atl2', heights[ROWS - 1][c])
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        print(pac, atl)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res


