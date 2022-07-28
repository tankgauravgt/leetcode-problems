# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildtree(nums):
            if not nums:
                return None
            
            hL = len(nums) // 2
            
            c = nums[hL]
            lx = buildtree(nums[0:hL])
            rx = buildtree(nums[1 + hL::])
            return TreeNode(c, lx, rx)
        
        return buildtree(nums)