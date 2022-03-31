# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head
        
        temp = ListNode(0, head)
            
        prev = temp
        curr = temp.next
        while curr and curr.next:
            tx = curr.next
            curr.next = curr.next.next
            prev.next = tx
            tx.next = curr
            prev = prev.next.next
            curr = curr.next
        
        return temp.next