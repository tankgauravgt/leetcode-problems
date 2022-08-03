class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        nums[-1] = 0
        target = len(nums) - 1
        for ix in range(len(nums) - 2, -1, -1):
            if ix + nums[ix] >= target:
                nums[ix] = 0
                target = ix
        
        if target == 0:
            return True
        else:
            return False