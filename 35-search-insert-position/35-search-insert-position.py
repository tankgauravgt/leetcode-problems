class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        less = True
        for ix, c in enumerate(nums):
            if c == target:
                return ix
        
        for ix, c in enumerate(nums):
            if c >= target:
                return ix
            
        return len(nums)