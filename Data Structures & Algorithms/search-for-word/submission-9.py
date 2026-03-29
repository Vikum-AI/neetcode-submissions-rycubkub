from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = len(board[0])
        y = len(board)
        
        visited = set()

        def dfs(i, j, char_index):
            nonlocal visited

            if char_index == len(word):
                return True

            if i < 0 or j < 0 or i >= y or j >= x:
                return False

            if (i, j) in visited:
                return False

            if board[i][j] != word[char_index]:
                return False

            print('True', board[i][j])

            visited.add((i, j))

            res = dfs(i+1, j, char_index+1) or dfs(i, j+1, char_index+1) or dfs(i-1, j, char_index+1) or dfs(i, j-1, char_index+1)

            visited.remove((i, j))

            return res


        for i in range(y):
            for j in range(x):
                if board[i][j].lower() == word[0].lower():
                    if dfs(i, j, 0):
                        return True


        return False
                    
