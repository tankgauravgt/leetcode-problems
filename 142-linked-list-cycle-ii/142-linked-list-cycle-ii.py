# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sx = fx = head
        
        start = True
        while sx and fx and fx.next:
            if not start and sx == fx:
                break
            sx = sx.next
            fx = fx.next.next
            start = False
        
        if fx and fx.next:
            px = head
            while sx != px:
                sx = sx.next
                px = px.next
            return px
        
        return None