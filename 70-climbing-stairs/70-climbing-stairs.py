class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        t1 = 1
        t2 = 2
        for ix in range(n - 2):
            t1, t2 = t2, t1 + t2
        return t2