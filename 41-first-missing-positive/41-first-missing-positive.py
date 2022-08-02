class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for ix, n in enumerate(nums):
            if n < 0:
                nums[ix] = 0
        
        for ix in range(len(nums)):
            if 1 <= abs(nums[ix]) <= len(nums):
                val = abs(nums[ix])
                if nums[val - 1] > 0:
                    nums[val - 1] = -1 * nums[val - 1]
                elif nums[val - 1] == 0:
                    nums[val - 1] = -(1 + len(nums))
        
        for ix in range(1, 1 + len(nums)):
            if nums[ix - 1] >= 0:
                return ix
        return 1 + len(nums)