# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def getdepth(node):
            if node:
                return 1 + max(getdepth(node.left), getdepth(node.right))
            return 0
        
        return getdepth(root)
        