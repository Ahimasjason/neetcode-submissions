# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        from collections import deque
        rv = []
        d = deque()
        d.append([root])

        while d:
            nodes = d.popleft()
            tmp = []
            nt = []
            for n in nodes:
                tmp.append(n.val )
                if n.left:
                    nt.append(n.left)
                if n.right:
                    nt.append(n.right)
            rv.append(tmp)
            if nt:
                d.append(nt)

        return rv
