# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tx = head
        while tx and tx.next:
            if tx.next.val == 0:
                tx = tx.next
            else:
                tx.val = tx.val + tx.next.val
                tx.next = tx.next.next
                continue
                
        tx = head
        while tx and tx.next:
            if tx.next.val == 0:
                tx.next = tx.next.next
            tx = tx.next
                    
        return head