# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        head = ListNode(0, head)
        temp = head
        
        count = 0
        while temp and temp.next:
            temp = temp.next
            count = count + 1
        
        if count < 2:
            return head.next
        
        if k >= count:
            k = k % count
        
        if k == 0:
            return head.next
            
        fast = head
        for ix in range(k):
            fast = fast.next
            
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head.next
        head = slow.next
        slow.next = None
        
        return head