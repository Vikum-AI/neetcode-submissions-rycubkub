# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # moment u have to go on both directions its the common anc
        # else its not 
        queue = deque()
        queue.append(root)

        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        while queue:
            node = queue.popleft()

            if not node:
                continue

            if node.val > max_val:
                queue.append(node.left)
                continue

            if node.val < min_val:
                queue.append(node.right)
                continue

            if node.val > min_val and node.val < max_val:
                return node

            if node.val == min_val or node.val == max_val:
                return node

        return TreeNode()
            

