# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(subTree, min_bound=float('-inf'), max_bound=float('inf')):
            if not subTree:
                return True
            
            if subTree.val <= min_bound or subTree.val >= max_bound:
                return False

            return isValid(subTree.left, min_bound, subTree.val) and isValid(subTree.right, subTree.val, max_bound)     

        return isValid(root)
