import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lx = bisect.bisect_left(nums, target, 0, len(nums))
        rx = bisect.bisect_right(nums, target, 0, len(nums))
        if lx < len(nums) and nums[lx] == target:
            return [lx, rx - 1]
        else:
            return [-1, -1]