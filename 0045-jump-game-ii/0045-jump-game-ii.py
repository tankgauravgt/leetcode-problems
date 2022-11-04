from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:

        lx = 0
        rx = 1
        count = 0
        while lx < rx:
            next_lx = rx
            next_rx = rx
            for cx in range(lx, rx):
                if cx == len(nums) - 1:
                    return count
                next_rx = max(next_rx, 1 + cx + nums[cx])
            lx = next_lx
            rx = next_rx
            count = count + 1
        
        return -1