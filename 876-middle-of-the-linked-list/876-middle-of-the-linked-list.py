# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        c = 0
        tx = head
        while tx != None:
            c = c + 1
            tx = tx.next
        
        tx = head
        for ix in range(c // 2):
            tx = tx.next
        
        return tx