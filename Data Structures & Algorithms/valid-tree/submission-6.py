class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit, path = set(), set()

        print(adj)

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)

            for val in adj[i]:
                if val == prev:
                    continue
                if not dfs(val, i):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n
