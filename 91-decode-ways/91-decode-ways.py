class Solution:
    def numDecodings(self, s: str) -> int:
        
        rec = {str(1 + ix):chr(ix + ord('a')) for ix in range(26)}
        
        memo = [-1] * (1 + len(s))
        def dfs(s, sx):
            nonlocal memo
            if sx == len(s):
                return 1
            elif memo[sx] != -1:
                return memo[sx]
            else:
                total = 0
                ex = 1 + sx
                while ex <= len(s) and s[sx:ex] in rec:
                    if memo[ex] == -1:
                        memo[ex] = dfs(s, ex)
                    total += memo[ex]
                    ex = ex + 1
                return total
        
        return dfs(s, 0)