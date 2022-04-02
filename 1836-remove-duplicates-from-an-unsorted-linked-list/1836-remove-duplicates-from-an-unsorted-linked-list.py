# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        rec = {}
        tx = head
        while tx:
            if rec.get(tx.val, None) == None:
                rec[tx.val] = 1
            elif rec.get(tx.val, None) != None:
                rec[tx.val] += 1
            tx = tx.next
        
        repeating = set(dict(filter(lambda x: x[1] > 1, rec.items())).keys())
        while head and head.val in repeating:
            head = head.next
        
        tx = head
        while tx and tx.next:
            if tx.next.val in repeating:
                tx.next = tx.next.next
                continue
            tx = tx.next
        
        return head