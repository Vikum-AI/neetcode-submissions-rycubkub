class Node:
    is_end = False

    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end


class WordDictionary:
    root = None
    sep = '.'

    def __init__(self):
        self.root = Node()

    def dfs(self, i, word, cur_node, count=4):
        if i >= len(word):
            cur_node.is_end = True
            return 

        if count > 0 and self.sep not in cur_node.children:
            cur_node.children[self.sep] = Node()

        if word[i] not in cur_node.children:
            cur_node.children[word[i]] = Node()

        self.dfs(i+1, word, cur_node.children[word[i]], count)

        if count > 0:
            self.dfs(i+1, word, cur_node.children[self.sep], count-1)


    def addWord(self, word: str) -> None:
        self.dfs(0, word, self.root)
        print(self.root)

    def search(self, word: str) -> bool:
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                return False
            
            cur_node = cur_node.children[c]

        return cur_node.is_end
        
