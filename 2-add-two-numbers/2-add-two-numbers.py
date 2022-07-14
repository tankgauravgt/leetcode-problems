# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         def solve(x1, x2, c):
            
#             if x1 and x2 and not x1.next and not x2.next:
#                 t1 = x2
#                 if c != 0:
#                     x2.next = ListNode(c)
#                 return
            
#             if x1 and not x1.next:
#                 x1.next = ListNode(0)
                
#             if x2 and not x2.next:
#                 x2.next = ListNode(0)
            
#             s = x1.next.val + x2.next.val + c
#             c = int(s / 10)
#             s = int(s % 10)
            
#             x1.next.val = s
#             x2.next.val = s
            
#             solve(x1.next, x2.next, c)
            
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         if l1 and l2:
#             ts = l1.val + l2.val
#             l1.val = ts % 10
#             l2.val = ts % 10
#             solve(l1, l2, ts // 10)
#         return l2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
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