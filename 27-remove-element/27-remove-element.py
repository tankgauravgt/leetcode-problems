class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        px = 0
        ctr = 0
        for ix, c in enumerate(nums):
            if c != val:
                nums[px] = c
                ctr += 1
                px += 1
            else:
                pass
            
        return ctr