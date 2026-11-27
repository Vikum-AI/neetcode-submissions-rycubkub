class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges))]
        rank = [1] * len(edges)

        
        def find(node):
            res = node

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return [n1+1, n2+1]

            if rank[r2] > rank[r1]:
                par[r1] = r2
                rank[r2] += 1
            else:
                par[r2] = r1
                rank[r1] += 1

            return None

        for u, v in edges:
            res = union(u - 1, v - 1)
            if res: return res


        return [-1, -1]