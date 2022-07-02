class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        cmax = 0
        curr = 0
        
        ix = 0
        while ix < len(nums):
            if nums[ix] == 1:
                curr = curr + 1
            else:
                curr = 0
            ix = ix + 1
            cmax = max(cmax, curr)
        
        return cmax