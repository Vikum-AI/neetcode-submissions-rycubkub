class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)

        def find(word):
            res = []
            
            for w in wordList:
                count = 0
                cond = True

                for i in range(len(w)):
                    if word[i] != w[i]:
                        count += 1

                        if count > 1:
                            cond = False
                            break
                    
                if cond: res.append(w)

            return res


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

                print(node)
                print(adj[node])

                if node == beginWord:
                    return res

                if node in seen:
                    continue

                seen.add(node)

                for nei in adj[node]:
                    if nei not in seen:
                        queue.append(nei)
            
        return 0
        

            