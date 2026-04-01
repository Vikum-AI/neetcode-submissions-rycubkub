import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        
        {
            "r1": [1, 2, 3]
            "c1": []
        }
        
        """

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        block_map = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]

                if value == '.':
                    continue
                
                if not (1 <= int(value) <= 9):
                    return False

                block = (math.ceil((r + 1) / 3), math.ceil((c + 1) / 3))

                if value in row_map[r] or value in col_map[c] or value in block_map[block]:
                    print(r, c, value)
                    print(block)
                    print(row_map, col_map, block_map)
                    print(value in row_map[r], value in col_map[c], value in block_map[block])
                    return False 

                row_map[r].add(value)
                col_map[c].add(value)   
                block_map[block].add(value)

        return True             
