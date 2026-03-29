class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])

        tl = (0, 0)
        tr = (0, COLS-1)

        bl = (ROWS-1, 0)
        br = (ROWS-1, COLS-1)

        elements = ROWS * COLS
        res = []

        """ 
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        """


        """
        [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
        ]
        """

        while len(res) < elements:
            # right to left
            for c in range(tl[1], tr[1]+1):
                res.append(matrix[tl[0]][c])
            # shift down
            tl = (tl[0]+1, tl[1])
            tr = (tr[0]+1, tr[1])

            if len(res) >= elements:
                break

            # top to bottom
            for r in range(tr[0], br[0]+1):
                res.append(matrix[r][tr[1]])
            # shift left
            tr = (tr[0], tr[1]-1)
            br = (br[0], br[1]-1)

            if len(res) >= elements:
                break

            # left to right
            for c in range(br[1], bl[1]-1, -1):
                res.append(matrix[br[0]][c])
            # shift up
            br = (br[0]-1, br[1])
            bl = (bl[0]-1, bl[1])

            if len(res) >= elements:
                break

            # bottom to top
            for r in range(bl[0], tl[0]-1, -1):
                print(r, tl[1])
                print(matrix[r][bl[1]])
                res.append(matrix[r][bl[1]])
            # shift right
            bl = (bl[0], bl[1]+1)
            tl = (tl[0], tl[1]+1)

        return res

