from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        head = ListNode(0, head)
        
        tx = head
        for ix in range(left):
            tx = tx.next
        
        buf = deque([])
        for ix in range(right - left + 1):
            buf.append(tx)
            tx = tx.next
        
        while len(buf) > 1:
            fx = buf.popleft()
            sx = buf.pop()
            fx.val, sx.val = sx.val, fx.val
        
        return head.next