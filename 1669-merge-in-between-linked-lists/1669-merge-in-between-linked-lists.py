# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        ax = list1
        for ix in range(a-1):
            ax = ax.next
        
        bx = list1
        for ix in range(b+1):
            bx = bx.next
        
        cx = list2
        while cx and cx.next:
            cx = cx.next
            
        if cx:
            cx.next = bx
        else:
            list2 = bx
        
        ax.next = list2
        
        return list1