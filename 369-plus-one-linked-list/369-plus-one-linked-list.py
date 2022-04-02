# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        rec = []
        tx = head
        while tx:
            rec += [tx]
            tx = tx.next
        
        s = 0
        c = 0
        ctr = 0
        for px in rec[::-1]:
            if ctr == 0:
                s = (1 + px.val + c)
                ctr += 1
            else:
                s = (px.val + c)
                ctr += 1
            c = s // 10
            px.val = (s % 10)
            if c == 0:
                break
            else:
                continue
        
        if c != 0:
            head = ListNode(c, head)
        
        return head