class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        cmax = 0
        
        lx = 0
        rx = len(height) - 1
        while rx > lx:
            area = min(height[lx], height[rx]) * (rx - lx)
            cmax = max(cmax, area)
            if height[lx] < height[rx]:
                lx = lx + 1
            else:
                rx = rx - 1
        
        return cmax