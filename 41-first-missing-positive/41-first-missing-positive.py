class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, 1 + len(nums)):
            if i not in nums:
                return i
        return 1 + len(nums)