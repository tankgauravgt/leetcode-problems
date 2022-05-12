# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        tx1 = list1
        tx2 = list2
        
        head = tx = ListNode(0, None)
        
        while tx1 and tx2:
            if tx1.val >= tx2.val:
                tx.next = ListNode(tx2.val)
                tx2 = tx2.next
            else:
                tx.next = ListNode(tx1.val)
                tx1 = tx1.next
            tx = tx.next
            
        while tx1:
            tx.next = ListNode(tx1.val)
            tx1 = tx1.next
            tx = tx.next
            
        while tx2:
            tx.next = ListNode(tx2.val)
            tx2 = tx2.next
            tx = tx.next
        
        return head.next