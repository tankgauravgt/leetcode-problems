class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        reachable = 0
        for ix, n in enumerate(nums):
            if ix > reachable:
                return False
            reachable = max(reachable, ix + n)
        return True