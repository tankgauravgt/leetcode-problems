class Solution:
    def numDecodings(self, s: str) -> int:
        
        rec = {str(1 + ix):chr(ix + ord('a')) for ix in range(26)}
        
        memo = {}
        def dfs(s, sx):
            nonlocal memo
            if sx == len(s):
                return 1
            elif sx in memo:
                return memo[sx]
            else:
                total = 0
                ex = 1 + sx
                while ex <= len(s) and s[sx:ex] in rec:
                    if ex not in memo:
                        memo[ex] = dfs(s, ex)
                    total += memo[ex]
                    ex = ex + 1
                memo[sx] = total
                return total
        
        return dfs(s, 0)