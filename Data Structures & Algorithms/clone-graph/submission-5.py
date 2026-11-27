"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned_map = defaultdict(Node)

        def dfs(n):
            if not n or not n.neighbors or n.val in cloned_map.keys():
                return

            clone = Node(n.val)
            cloned_map[n.val] = clone

            for nei in n.neighbors:
                dfs(nei)

            for nei in n.neighbors:
                clone.neighbors.append(cloned_map[nei.val])

        dfs(node)

        return cloned_map[1]