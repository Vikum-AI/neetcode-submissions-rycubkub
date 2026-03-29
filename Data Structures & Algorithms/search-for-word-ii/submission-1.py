class PrefixNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = PrefixNode()
        
        for word in words:
            root.insert(word)

        visit = set()
        res = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            if (r >= ROWS or c >= COLS
                or r < 0 or c < 0 
                or (r, c) in visit
                or board[r][c] not in node.children):
                return


            visit.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.is_end:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
            



        
    