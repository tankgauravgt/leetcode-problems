class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 2: return n
        
        l1, l2 = 1, 2
        for ix in range(n - 2):
            l2, l1 = l1 + l2, l2
        return l2