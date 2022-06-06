class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        for ix, n in enumerate(nums):
            nums[ix] = nums[ix] + prev
            prev = nums[ix]
        return nums