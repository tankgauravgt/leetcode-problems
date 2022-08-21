from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        lx = 0
        taken = 0
        for rx, n in enumerate(nums):
            if rx == 0:
                nums[lx] = nums[rx]
                taken = taken + 1
                lx = lx + 1
                continue
            elif nums[rx] != nums[rx - 1] or taken < 2:
                if nums[rx] == nums[rx - 1]:
                    taken = taken + 1
                else:
                    taken = 1
                nums[lx] = nums[rx]
                lx = lx + 1
        
        return lx