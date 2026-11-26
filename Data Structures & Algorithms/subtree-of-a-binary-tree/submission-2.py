# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:return True
        if (root and not subRoot) or  subRoot and not root:return False

        
        def find_root(node, sn):

            if not sn:return True
            if not node:return False


            return dfs(node, sn) or find_root(node.left, sn) or find_root(node.right, sn)

        

        def dfs(l, r):
            if not l and not r:return True

            if l and r and l.val == r.val:
                return dfs(l.left, r.left) and dfs(l.right, r.right)

            return False


        return find_root(root, subRoot)