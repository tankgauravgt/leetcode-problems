class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lbinsearch(nums, lx, rx, target):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if target > nums[mx]:
                    return lbinsearch(nums, mx + 1, rx, target)
                elif target < nums[mx]:
                    return lbinsearch(nums, lx, mx - 1, target)
                else:
                    ix = lbinsearch(nums, lx, mx - 1, target)
                    if ix == -1:
                        return mx
                    else:
                        return ix
            return -1
        
        def rbinsearch(nums, lx, rx, target):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if target > nums[mx]:
                    return rbinsearch(nums, mx + 1, rx, target)
                elif target < nums[mx]:
                    return rbinsearch(nums, lx, mx - 1, target)
                else:
                    ix = rbinsearch(nums, mx + 1, rx, target)
                    if ix == -1:
                        return mx
                    else:
                        return ix
            return -1
        
        if len(nums) > 0:
            return [lbinsearch(nums, 0, len(nums) - 1, target), rbinsearch(nums, 0, len(nums) - 1, target)]
        else:
            return [-1, -1]