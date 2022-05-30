# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        leq = lx = ListNode()
        geq = gx = ListNode()
        
        tx = head
        while tx:
            if tx.val < x:
                lx.next = ListNode(tx.val)
                lx = lx.next
            else:
                gx.next = ListNode(tx.val)
                gx = gx.next
            tx = tx.next
        
        lx.next = geq.next
        return leq.next