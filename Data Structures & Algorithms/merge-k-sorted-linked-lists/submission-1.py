# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None
        
        def sort_node(n1,n2):
            dummy = ListNode()
            tail = dummy

            while n1 and n2:
                if n1.val < n2.val:
                    tail.next = n1
                    n1 = n1.next
                else:
                    tail.next = n2
                    n2  = n2.next
                tail = tail.next
            if n1:
                tail.next = n1
            if n2:
                tail.next = n2
            return dummy.next


        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(sort_node(l1, l2))
            lists = merged_lists

        return lists[0]