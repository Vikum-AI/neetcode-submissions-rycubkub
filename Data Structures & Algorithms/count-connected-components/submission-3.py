class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n


        # find root parent of n1
        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            r1, r2 = rank[n1], rank[n2]

            if n1 == n2:
                return 0

            if r1 > r2:
                par[n2] = n1
                rank[n2] += rank[n1]
            else:
                par[n1] = n2
                rank[n1] += rank[n2]

            return 1

        res = n

        for n1, n2 in edges:
            res -= union(n1, n2)
    
        return res
            