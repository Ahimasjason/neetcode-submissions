# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs_approach(self, root)-> int:
        def dfs(node):
            if not node:return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + max(left, right)

        return dfs(root)

    def iterative(self, root):
        if not root:return 0

        rv = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                rv = max(rv, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return rv
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # return self.dfs_approach(root)
        return self.iterative(root)

        