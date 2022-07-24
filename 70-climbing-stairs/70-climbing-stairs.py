class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def rec(n):
            nonlocal memo
            if n <= 2:
                return n
            if n not in memo:
                memo[n] = rec(n - 1) + rec(n - 2)
            return memo[n]
        
        return rec(n)