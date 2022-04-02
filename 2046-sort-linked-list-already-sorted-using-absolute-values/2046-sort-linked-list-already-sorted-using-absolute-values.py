# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rec = []
        while head and head.val < 0:            
            rec += [head.val]
            head = head.next
        
        tx = head
        while tx and tx.next:
            if tx.next.val < 0:
                rec += [tx.next.val]
                tx.next = tx.next.next
                continue
            tx = tx.next
        
        for n in sorted(rec)[::-1]:
            head = ListNode(n, head)
        
        return head