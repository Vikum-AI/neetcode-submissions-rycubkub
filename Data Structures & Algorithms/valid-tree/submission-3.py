class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)

            for n in adj[node]:
                if n == prev:
                    continue
                print(n)
                if not dfs(n, node):
                    return False

            return True

        count = 0

        for i in range(n):
            if i not in visit:
                count += 1
                res = dfs(i, -1)
                print(visit)
                if not res:
                    return False

        return count == 1 


