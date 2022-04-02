# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        c = 0
        tx = head
        while tx:
            c += 1
            tx = tx.next
        
        t = 0
        bx1 = None
        tx = head
        while tx:
            if (t+1) == k:
                if bx1:
                    bx1.val, tx.val = tx.val, bx1.val
                else:
                    bx1 = tx
            elif (c-t) == k:
                if bx1:
                    bx1.val, tx.val = tx.val, bx1.val
                else:
                    bx1 = tx
            t = t + 1
            tx = tx.next
        
        return head