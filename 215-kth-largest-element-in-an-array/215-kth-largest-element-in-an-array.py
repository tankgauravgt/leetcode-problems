import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def qselect(nums, lx, rx):
            px = lx
            for ix in range(lx, rx):
                if nums[ix] <= nums[rx]:
                    nums[ix], nums[px] = nums[px], nums[ix]
                    px = px + 1
            nums[rx], nums[px] = nums[px], nums[rx]
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