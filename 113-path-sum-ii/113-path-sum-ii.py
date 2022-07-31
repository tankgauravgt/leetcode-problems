# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        def btrack(node, arr, s):
            nonlocal res
            if not node.left and not node.right:
                if s == (targetSum - node.val):
                    res.append(arr.copy() + [node.val])
                return
            if node.left:
                s = s + node.val
                arr.append(node.val)
                btrack(node.left, arr, s)
                arr.pop()
                s = s - node.val
            if node.right:
                s = s + node.val
                arr.append(node.val)
                btrack(node.right, arr, s)
                arr.pop()
                s = s - node.val
        
        btrack(root, [], 0)
        return res