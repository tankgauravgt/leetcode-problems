# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        n = 0
        tx = head
        while tx != None:
            n = n + 1
            tx = tx.next
        
        arr = [0 for i in range(n)]
        
        ix = 0
        tx = head
        while tx != None:
            if ix < n // 2:
                arr[ix] += tx.val
            else:
                arr[n - ix - 1] += tx.val
            ix = ix + 1
            tx = tx.next
        
        return max(arr)