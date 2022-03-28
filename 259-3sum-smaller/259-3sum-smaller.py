import bisect

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 3:
            return 0
        
        nums = sorted(nums)
        
        count = 0
        for lx in range(len(nums) - 2):
            for cx in range(lx+1, len(nums) - 1):
                count += (bisect.bisect_left(nums, target - (nums[lx] + nums[cx]), cx+1) - 1 - cx)
                
        return count