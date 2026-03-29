# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(node, current_depth=0):
            if not node:
                return current_depth

            current_depth += 1

            left_depth = dfs(node.left, current_depth)
            right_depth = dfs(node.right, current_depth)

            max_depth = max(left_depth or 0, right_depth or 0)

            return max_depth

        return dfs(root)

