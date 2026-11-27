"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(n):
            if n.val in clone.keys():
                return clone[n.val]

            clone_node = Node(n.val)
            clone[n.val] = clone_node

            for nei in n.neighbors:
                clone_node.neighbors.append(dfs(nei))

            return clone_node

        return dfs(node) if node else None