class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        px = 0
        ctr = 0
        last = None
        for ix, c in enumerate(nums):
            if c != last:
                nums[px] = c
                px += 1
                ctr += 1
            last = c
        
        return ctr