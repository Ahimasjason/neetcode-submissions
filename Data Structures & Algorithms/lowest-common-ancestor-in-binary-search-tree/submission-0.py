# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def helper(r, n0, n1):
            if not r:return 0, None

            lr = helper(r.left, n0,n1)
            if lr[0] == 2:
                return lr

            rr = helper(r.right, n0,n1)
            if rr[0] == 2:
                return rr

            cr = lr[0] + rr[0] + (1 if n0.val == r.val else 0) + (1 if n1.val == r.val else 0)
            # print("root.val = " , r.val, cr , lr, rr)
            return cr, r if  cr == 2 else None
        return helper(root, p, q)[1]


                
