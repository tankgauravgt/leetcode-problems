class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 1:
            return 0
        
        lmax = 0
        rmax = max(height[1::])
        
        total = 0
        for cx, n in enumerate(height):
            if cx == 0:
                continue
            lmax = max(lmax, height[cx - 1])
            if rmax == height[cx]:
                if height[1 + cx::]:
                    rmax = min(rmax, max(height[1 + cx::]))
            if (min(lmax, rmax) - height[cx]) > 0:
                total = total + (min(lmax, rmax) - height[cx])
            
        return total