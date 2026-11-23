# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        next_node = ListNode(0)
        dummy = ListNode(0, next_node)

        l1_curr = l1
        l2_curr = l2
        while l1_curr or l2_curr:
            v1 = l1_curr.val if l1_curr else 0
            v2 = l2_curr.val if l2_curr  else 0
            sum = v1 + v2 + carry
            next_node.val = sum % 10
            carry = sum // 10
            if l1_curr:
                l1_curr = l1_curr.next
            
            if l2_curr:
                l2_curr = l2_curr.next
            if l1_curr or l2_curr:
                nn = ListNode(0)
                next_node.next = nn
                next_node = nn
            if not l1_curr and not l2_curr and carry != 0:
                # print("coming here")
                nn = ListNode(carry)
                next_node.next = nn
                next_node = nn

        return dummy.next
        

        