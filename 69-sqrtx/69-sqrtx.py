class Solution:
    def mySqrt(self, x: int) -> int:
        
        gx = 0
        for i in range(100000000000000):
            if x > (i * i):
                pass
            else:
                gx = i
                break
        
        return gx if (gx * gx == x) else (gx - 1)