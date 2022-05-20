class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if sorted(nums, reverse=True) == nums:
            nums.sort()
        else:
            lx = len(nums) - 2
            while nums[lx + 1] <= nums[lx] and lx >= 0:
                lx = lx - 1
            mx = lx + 1
            for ix in range(mx, len(nums), 1):
                if nums[ix] > nums[lx] and nums[ix] < nums[mx]:
                    mx = ix
            nums[lx], nums[mx] = nums[mx], nums[lx]
            nums[lx + 1::] = sorted(nums[lx + 1::])