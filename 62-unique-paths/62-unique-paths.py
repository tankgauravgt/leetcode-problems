class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {(0, 0): 1}
        for rx in range(m):
            for cx in range(n):
                if (rx, cx) in memo:
                    continue
                if rx == 0:
                    memo[(rx, cx)] = memo[(rx, cx - 1)]
                elif cx == 0:
                    memo[(rx, cx)] = memo[(rx - 1, cx)]
                else:
                    memo[(rx, cx)] = memo[(rx, cx - 1)] + memo[(rx - 1, cx)]
        
        return memo[(m - 1, n - 1)]