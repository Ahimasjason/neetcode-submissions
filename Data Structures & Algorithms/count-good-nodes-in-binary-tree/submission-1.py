# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:return None

        rv = 0
        def dfs(node, pre_max):
            nonlocal rv
            if not node:return 
            if node.val >= pre_max:
                rv+=1
            
            next_max = max(pre_max, node.val)
            dfs(node.left, next_max)
            dfs(node.right, next_max)

        dfs(root, root.val)
        return rv