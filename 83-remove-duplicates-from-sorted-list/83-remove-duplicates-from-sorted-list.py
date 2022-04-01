# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tx = head
        while tx and tx.next:
            while tx and tx.next and tx.val == tx.next.val:
                tx.next = tx.next.next
            if tx:
                tx = tx.next
        return head