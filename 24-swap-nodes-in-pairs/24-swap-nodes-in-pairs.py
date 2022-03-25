# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        if head.next == None:
            return head
        else:
            temp = tx = ListNode(0, head)
            
            ix = 0            
            while tx.next and tx.next.next:
                bx = tx.next.next.next
                if ix % 2 == 0:
                    p1 = tx.next
                    p2 = tx.next.next
                    p1.next = bx
                    p2.next = p1
                    tx.next = p2
                tx = tx.next.next
            
            return temp.next