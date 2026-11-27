# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:return []

        d = deque()
        d.append([root])
        rv = []

        while d:
            le = d.popleft()

            nl = []
            
            for n in le:
                if n.left:
                    nl.append(n.left)
                if n.right:
                    nl.append(n.right)

            ln = le.pop()
            if ln:
                rv.append(ln.val)
            if nl:
                d.append(nl)
        return rv
