# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, left, right):
            
            if not node:return True

            if not (left < node.val < right):
                return False


            left_t = dfs(node.left, left , node.val )
            right_t = dfs(node.right, node.val, right)

            return left_t and right_t
        return dfs(root, float("-inf"), float("inf"))