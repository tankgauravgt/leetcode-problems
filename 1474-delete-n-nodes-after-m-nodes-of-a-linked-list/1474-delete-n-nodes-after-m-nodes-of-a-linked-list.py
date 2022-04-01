# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        temp = tx = head
        
        while tx and tx.next:
        
            for ix in range(m - 1):
                if tx:
                    print('Keep', tx.val)
                    tx = tx.next
                else:
                    break
                    
            for ix in range(n):            
                if tx and tx.next:
                    tx.next = tx.next.next
                else:
                    break
            
            if tx:
                tx = tx.next
        
        return temp