# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def recurse(self, head):
        if (head == None) or (head.next == None):
            return head
        px = self.recurse(head.next)
        head.next.next = head
        head.next = None
        return px
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(head)