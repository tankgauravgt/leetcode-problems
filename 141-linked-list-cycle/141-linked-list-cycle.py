# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next
        
        while True:
            
            if not slow or not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if slow and fast and slow == fast:
                return True
            
        return False