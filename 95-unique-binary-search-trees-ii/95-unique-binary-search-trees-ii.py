# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def genTrees(lx, rx):
            if rx <= lx:
                return [None]
            res = []
            for ix in range(lx, rx):
                ltrees = genTrees(lx, ix)
                rtrees = genTrees(1 + ix, rx)
                for ltree in ltrees:
                    for rtree in rtrees:
                        res.append(TreeNode(ix, ltree, rtree))
            return res
            
        results = genTrees(1, n + 1)
        return results