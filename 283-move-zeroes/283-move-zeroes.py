class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lx = 0
        for rx, n in enumerate(nums):
            if nums[rx] != 0:
                nums[lx], nums[rx] = nums[rx], nums[lx]
                lx = lx + 1
        
        return nums