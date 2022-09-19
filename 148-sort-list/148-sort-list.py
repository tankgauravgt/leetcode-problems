# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rec = []
        while head:
            rec.append(head.val)
            head = head.next
        
        rec.sort()
        
        tx = head = ListNode(0, None)
        for node in rec:
            tx.next = ListNode(node, None)
            tx = tx.next
        
        return head.next