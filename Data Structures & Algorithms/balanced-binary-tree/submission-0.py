# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:return -1, True

            (left, lb) = dfs(node.left)
            right, rb = dfs(node.right)
            if not lb or not rb:return 0,False
            height = max(left, right) + 1
            is_bal = abs(left - right) <= 1
            return (height, is_bal)


        return dfs(root)[1]