class Node:
    val: str = None
    children = []
    is_end: bool = False

    def __init__(self, val=None, children=[], is_end=False):
        self.val = val
        self.children = children
        self.is_end = is_end



class PrefixTree:
    head = None

    def __init__(self):
        self.head = self._init_node()

    def _init_node(self, val=None, is_end=False):
        children = [None] * 26
        return Node(val=val, children=children, is_end=is_end)

    def insert(self, word: str) -> None:
        cur_level = self.head
        word_len = len(word)

        for i, c in enumerate(word):
            c_val = ord('a') - ord(c)
            node = cur_level.children[c_val]
            is_end = i + 1 == word_len

            if not node:
                node = self._init_node(val=c_val)
                cur_level.children[c_val] = node

            if is_end:
                node.is_end = True
                # cur_level.children[c_val] = node

            cur_level = node


    def search(self, word: str) -> bool:
        return self.startsWith(word, is_whole=True)
        

    def startsWith(self, prefix: str, is_whole=False) -> bool:
        cur_level = self.head
        word_len = len(prefix)

        for i, c in enumerate(prefix):
            c_val = ord('a') - ord(c)
            node = cur_level.children[c_val]

            if not node:
                return False

            if is_whole and i + 1 == word_len:
                if not node.is_end:
                    return False

            cur_level = node

        return True
        
        