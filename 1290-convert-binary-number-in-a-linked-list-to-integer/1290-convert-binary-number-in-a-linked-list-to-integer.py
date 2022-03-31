# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        s = 0
        ix = 0
        while head:
            s = 2 * s + int(head.val)
            ix = ix + 1
            head = head.next
        return s