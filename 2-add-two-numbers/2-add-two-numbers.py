# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tx = l1
        L1 = l1
        L2 = l2
        rx = None
        
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            c = s // 10
            l1.val = s % 10
            l2.val = s % 10
            tx = l1
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = l1.val + c
            c = s // 10
            l1.val = (s % 10)
            tx = l1
            l1 = l1.next
            rx = L1
            
        while l2:
            s = l2.val + c
            c = s // 10
            l2.val = (s % 10)
            tx = l2
            l2 = l2.next
            rx = L2
        
        if not rx:
            rx = L1
        
        if c != 0:
            tx.next = ListNode(c)
        
        return rx