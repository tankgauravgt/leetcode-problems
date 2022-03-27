# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # output:
        outdata = []
        
        # context manager
        context = []
        
        ptr = root
        while len(context) > 0 or ptr != None:
            
            # process current node and its left subtree recursively.
            while ptr != None:
                context += [{'node': ptr}]
                ptr = ptr.left
            
            # take last element:
            ptr = context.pop()['node']

            # store values:
            outdata += [ptr.val]
            
            # process right element:
            ptr = ptr.right
            
        return outdata