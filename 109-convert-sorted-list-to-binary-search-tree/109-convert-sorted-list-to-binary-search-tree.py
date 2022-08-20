# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        to_arr = []
        while head:
            to_arr.append(head.val)
            head = head.next
        
        def to_bst(arr):
            if len(arr) == 0:
                return None
            
            hL = len(arr) // 2
            
            node = TreeNode(arr[hL])
            
            node.left = to_bst(arr[0:hL])
            node.right = to_bst(arr[1 + hL::])
            
            return node
        
        return to_bst(to_arr)