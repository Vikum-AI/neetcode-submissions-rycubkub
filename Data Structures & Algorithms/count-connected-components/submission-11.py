class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        res = 0
        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for values in adj_list[node]:
                dfs(values)

            

        for key in adj_list.keys():
            if key not in visit:
                res += 1
                dfs(key)

        return res + n - len(visit) 