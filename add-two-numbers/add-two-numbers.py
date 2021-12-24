# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        out = tmp = ListNode()
        while l1 != None or l2 != None:
            acc = carry
            if l1 != None:
                acc += l1.val
                l1 = l1.next
            if l2 != None:
                acc += l2.val
                l2 = l2.next
            tmp.next = ListNode(acc % 10)
            carry = acc // 10
            tmp = tmp.next
                
        if carry != 0:
            tmp.next = ListNode(carry)
        
        return out.next