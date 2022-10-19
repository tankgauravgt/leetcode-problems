# Definition for singly-linked list.
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev_k(node, k):
            prev = None
            curr = node
            while node and k > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k = k - 1
            return prev
        
        result = last = ListNode(0, None)
        
        curr_group = head
        while curr_group:
            next_group = curr_group
            flag = True
            for ix in range(k):
                if not next_group:
                    flag = False
                    break
                next_group = next_group.next
            
            if flag:
                last.next = rev_k(curr_group, k)
            else:
                last.next = curr_group
            
            while last and last.next:
                    last = last.next
            
            curr_group = next_group
        
        return result.next