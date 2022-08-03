class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 2:
            return 0
        
        cmax = 0
        lmax = []
        for ix, n in enumerate(height):
            cmax = max(cmax, n)
            lmax.append(cmax)
        
        cmax = 0
        rmax = []
        for ix, n in enumerate(height[::-1]):
            cmax = max(cmax, n)
            rmax.append(cmax)
        rmax = rmax[::-1]
        
        total = 0
        for cx, n in enumerate(height):
            if cx == 0 or cx == len(height) - 1:
                continue
            if (min(lmax[cx - 1], rmax[cx + 1]) - n) > 0:
                total = total + (min(lmax[cx - 1], rmax[cx + 1]) - n)
            
        return total