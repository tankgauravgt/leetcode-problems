class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cmax = 0
        for ix in range(1, len(nums), 1):
            nums[ix] = nums[ix] + cmax
            cmax = max(cmax, nums[ix - 1])
        
        return max(cmax, nums[-1])