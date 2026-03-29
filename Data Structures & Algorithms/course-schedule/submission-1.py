class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for preq in prerequisites:
            adj[preq[0]].append(preq[1])

        visit = set()

        def dfs(crs):
            if (crs in visit):
                return False
            
            if not adj[crs]:
                return True

            visit.add(crs)
            for val in adj[crs]:
                if not dfs(val):
                    return False
                
            visit.remove(crs)
            adj[crs] = []
            return True
             
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


