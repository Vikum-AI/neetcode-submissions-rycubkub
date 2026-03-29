class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for crs, preq in prerequisites:
            adj[crs].append(preq)

        visit = set()

        def dfs(c):
            if c in visit:
                return False

            if not adj[c]:
                return True

            visit.add(c)
            for preq in adj[c]:
                if not dfs(preq):
                    return False

            adj[c] = []
            visit.remove(c)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

