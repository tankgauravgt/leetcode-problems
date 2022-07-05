class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for ix in range(len(nums) - 3, -1, -1):
            if nums[ix] + nums[ix + 1] > nums[ix + 2]:
                return sum(nums[ix:ix+3])
        return 0