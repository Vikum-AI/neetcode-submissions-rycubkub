"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        head = node

        clone_map = {}

        def dfs(n):
            if n in clone_map:
                return clone_map[n]

            if not n:
                return

            clone_node = Node(n.val)
            clone_map[n] = clone_node

            neis = []

            for nei in n.neighbors:
                nei_node = dfs(nei)
                neis.append(nei_node)

            clone_node.neighbors = neis

            return clone_node

        dfs(node)

        return clone_map[node] if node else None
