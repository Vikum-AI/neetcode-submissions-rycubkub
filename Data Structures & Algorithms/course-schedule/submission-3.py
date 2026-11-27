class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        adj = defaultdict(list)
        order = []

        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1
            in_degree[b] = in_degree[b] if in_degree[b] else 0


        def bfs():
            queue = deque()

            for key, val in in_degree.items():
                if val == 0:
                    queue.append(key)

            while queue:
                node = queue.popleft()
                order.append(node)

                for nei in adj[node]:
                    in_degree[nei] -= 1

                    if in_degree[nei] == 0:
                        queue.append(nei)

        bfs()

        for in_degree in in_degree.values():
            if in_degree != 0:
                return False

        return True



