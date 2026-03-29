class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(r + 1, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

