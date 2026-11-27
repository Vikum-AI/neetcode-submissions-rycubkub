import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)

        wordSet = set(wordList)

        def find(word):
            comb = []

            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    comp_word = word[:i] + char + word[i+1:]
                    
                    if comp_word in wordSet:
                        comb.append(comp_word)

            return comb


        def construct_graph():
            for w in wordList:
                adj[w] += find(w)


        construct_graph()

        res = 0
        
        queue = deque()
        queue.append(endWord)
        seen = set()

        while queue:
            size = len(queue)
            res += 1

            for i in range(size):
                node = queue.popleft()

                if node == beginWord:
                    return res

                if node in seen:
                    continue
                    
                for nei in adj[node]:
                    if nei not in seen:
                        seen.add(node)
                        queue.append(nei)
            
        return 0
        

            