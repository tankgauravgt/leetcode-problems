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

        ttx = tx
        values = deque([])
        for ix in range(right - left + 1):
            values.append(ttx)
            ttx = ttx.next
        
        while len(values) > 1:
            fx = values.popleft()
            sx = values.pop()
            fx.val, sx.val = sx.val, fx.val
        
        return head.next