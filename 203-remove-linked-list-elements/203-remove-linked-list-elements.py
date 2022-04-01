# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        tx = head
        while tx and tx.next:
            if tx.next.val == val:
                tx.next = tx.next.next
            else:
                tx = tx.next

        while head and head.val == val:
            head = head.next
            
        return head