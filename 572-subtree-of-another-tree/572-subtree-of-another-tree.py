# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.temp = []

    def preorder(self, root):
        if not root:
            return
        self.temp += [root.val]
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.temp += [root.val]
        self.inorder(root.right)
    
    def recursive_check(self, root, candidate):
        if root == None:
            return False
        
        self.temp = []
        self.inorder(candidate)
        cd_iot = self.temp.copy()
        
        self.temp = []
        self.inorder(root)
        rf_iot = self.temp.copy()
        
        self.temp = []
        self.preorder(candidate)
        cd_pot = self.temp.copy()
        
        self.temp = []
        self.preorder(root)
        rf_pot = self.temp.copy()
        
        if (cd_iot == rf_iot) and (cd_pot == rf_pot):
            return True
        else:
            return self.recursive_check(root.left, candidate) or self.recursive_check(root.right, candidate)
        
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.recursive_check(root, subRoot)