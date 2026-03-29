class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visit = set()
        adj = defaultdict(list)

        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)


        print(adj)


        def dfs(node):
            if node in visit:
                return 

            visit.add(node)

            for nei in adj[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                print(i, visit)
                res += 1

        return res
