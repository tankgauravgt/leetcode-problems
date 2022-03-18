# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hx = ListNode(0, head)
        hx = self.recurse(hx, hx.next, [0], n)  
        return hx.next
    
    
    def recurse(self, px, cx, ctx, target):
        if cx != None:
            px.next = self.recurse(cx, cx.next, ctx, target)
        ctx[0] = ctx[0] + 1
        return px if (ctx[0] != target) else cx