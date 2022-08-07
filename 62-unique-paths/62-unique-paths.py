import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m < n:
            return self.uniquePaths(n, m)
        
        f = math.factorial
        
        return int(f(m + n - 2) / (f(m - 1) * f(n - 1)))