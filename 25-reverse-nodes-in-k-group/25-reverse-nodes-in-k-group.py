# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def len_gt_k(self, head, k):
        tx = head
        for ix in range(k + 1):
            if tx:
                tx = tx.next
            else:
                return False
        return True
    
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = px = ListNode(0, head)
        
        while self.len_gt_k(px, k):
            buf = []
            tx = px.next
            for ix in range(k + 1):
                buf += [tx]
                # print(tx)
                if tx:
                    tx = tx.next
            
            for ix in range(k - 1):
                buf[ix + 1].next = buf[ix]
            buf[0].next = buf[-1]
            
            px.next = buf[-2]
            
            for ix in range(k):
                px = px.next
        
        return temp.next