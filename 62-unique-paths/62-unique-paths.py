import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for mx in range(m)]
        
        for mx in range(m):
            dp[mx][0] = 1
        for nx in range(n):
            dp[0][nx] = 1
        
        for mx in range(1, m):
            for nx in range(1, n):
                dp[mx][nx] = dp[mx - 1][nx] + dp[mx][nx - 1]
        
        return dp[m - 1][n - 1]