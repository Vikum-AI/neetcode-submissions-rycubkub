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

        if not node.neighbors:
            return Node(val=node.val)

        adj = defaultdict(list)

        visit = set()

        def build_adj(cur_node):
            if not cur_node:
                return

            if cur_node.val in visit:
                return 

            visit.add(cur_node.val)

            if not cur_node.neighbors:
                adj[cur_node.val] = []
                return 

            for neighbor in cur_node.neighbors:
                adj[cur_node.val].append(neighbor.val)
                build_adj(neighbor)


        build_adj(node)

        nodes = defaultdict(Node)

        for key in adj.keys():
            nodes[key] = Node(val=key)

        for key, vals in adj.items():
            n = []
            for val in vals:
                n.append(nodes[val])

            nodes[key].neighbors = n

        return nodes[1]






