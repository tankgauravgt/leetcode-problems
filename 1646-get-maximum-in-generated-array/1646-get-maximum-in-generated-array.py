class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n < 2:
            return n
        
        memo = [-1] * (1 + n)
        
        memo[0] = 0
        memo[1] = 1
        for ix in range(2, 1 + n):
            if ix % 2 == 0:
                memo[ix] = memo[ix // 2]
            elif ix % 2 == 1:
                memo[ix] = memo[ix // 2] + memo[1 + (ix // 2)]
        
        return max(memo)