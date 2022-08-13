class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 2:
            return 0
        
        lx = 0
        rx = len(height) - 1
        
        lmax = height[lx]
        rmax = height[rx]
        
        total = 0
        while rx > lx:
            if height[rx] <= height[lx]:
                if height[rx] < rmax:
                    total = total + (rmax - height[rx])
                rmax = max(rmax, height[rx])
                rx = rx - 1
            else:
                if height[lx] < lmax:
                    total = total + (lmax - height[lx])
                lmax = max(lmax, height[lx])
                lx = lx + 1
        
        return total