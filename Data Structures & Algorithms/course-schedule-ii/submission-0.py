class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        adj = defaultdict(list)

        for a, b in prerequisites:
            in_degree[a] += 1 
            adj[b].append(a)

        order = []
        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return order if len(order) == numCourses else []

            
            

