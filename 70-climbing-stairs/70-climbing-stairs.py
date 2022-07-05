class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dp(n, memo):
            if n <= 2:
                return n
            else:
                if (n - 1) not in memo:
                    memo[n - 1] = dp(n - 1, memo)
                if (n - 2) not in memo:
                    memo[n - 2] = dp(n - 2, memo)
                return memo[n - 1] + memo[n - 2]
        
        return dp(n, {})