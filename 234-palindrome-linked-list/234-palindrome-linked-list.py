# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        out = ""
        tx = head
        while tx:
            out += str(tx.val)
            tx = tx.next
        print(out)
        return out == out[::-1]