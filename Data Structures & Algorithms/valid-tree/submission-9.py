class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        
        def dfs(node, prev=None):
            if node != prev and node in seen:
                return False

            seen.add(node)

            for nei in adj_list[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False

            return True


        if not dfs(0):
            return False

        return len(seen) == n