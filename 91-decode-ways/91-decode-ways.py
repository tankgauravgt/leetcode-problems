class Solution:
    def numDecodings(self, s: str) -> int:
        
        rec = {str(1 + ix):chr(ix + ord('a')) for ix in range(26)}
        
        memo = {}
        def dfs(s, sx):
            nonlocal memo
            if sx == len(s):
                memo[sx] = 1
                return memo[sx]
            elif sx in memo:
                return memo[sx]
            else:
                total = 0
                for ix in range(2):
                    if (sx + ix + 1) <= len(s) and s[sx:sx + ix + 1] in rec:
                        if (sx + ix + 1) not in memo:
                            memo[sx + ix + 1] = dfs(s, sx + ix + 1)
                        total += memo[sx + ix + 1]
                    else:
                        break
                return total
        
        return dfs(s, 0)