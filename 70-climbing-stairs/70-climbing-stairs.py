class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def rec(k):
            nonlocal n, memo
            if k >= (n - 2):
                return n - k
            if k not in memo:
                memo[k] = rec(k + 1) + rec(k + 2)
            return memo[k]
        
        return rec(0)