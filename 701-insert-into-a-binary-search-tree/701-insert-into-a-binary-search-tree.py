# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        
        temp = root
        while temp:
            if val < temp.val:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = TreeNode(val)
                    return root
            if val > temp.val:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = TreeNode(val)
                    return root
        return TreeNode(val)