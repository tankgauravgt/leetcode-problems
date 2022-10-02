import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def qselect(nums, lx, rx):
            px = ix = lx
            while ix < rx:
                if nums[ix] <= nums[rx]:
                    nums[ix], nums[px] = nums[px], nums[ix]
                    px = px + 1
                    ix = ix + 1
                else:
                    ix = ix + 1
            nums[ix], nums[px] = nums[px], nums[ix]
            return px
        
        lx = 0
        rx = len(nums) - 1
        
        px = -1
        while px != len(nums) - k:
            px = qselect(nums, lx, rx)
            if px < len(nums) - k:
                lx = px + 1
            else:
                rx = px - 1
        
        return nums[px]