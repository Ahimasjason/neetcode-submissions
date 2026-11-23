"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d  = {}
        
        curr = head
        while curr:
            nn = Node(curr.val)
            d[curr] = nn
            curr = curr.next
        

        cur = head
        while cur:
            no = d[cur]
            no.next = d.get(cur.next)
            no.random = d.get(cur.random)
            cur = cur.next


        return d.get(head)
        