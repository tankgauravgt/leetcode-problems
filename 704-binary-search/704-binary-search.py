class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binsearch(nums, lx, rx, target):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if target < nums[mx]:
                    return binsearch(nums, lx, mx - 1, target)
                elif target > nums[mx]:
                    return binsearch(nums, mx + 1, rx, target)
                else:
                    return mx
            return -1
        
        return binsearch(nums, 0, len(nums) - 1, target)