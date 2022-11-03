import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        Np, Ns = len(p), len(s)
        memo = [[-1] * (1 + Np) for sx in range(1 + Ns)]
        
        def rex_match2(s, p, sx, px, memo):
            if px == len(p):
                return sx == len(s)
            if memo[sx][px] != -1:
                return memo[sx][px]
            match = sx < len(s) and p[px] in {s[sx], '.'}
            if px < len(p) - 1 and p[1 + px] == '*':
                memo[sx][px] = (rex_match2(s, p, sx, 2 + px, memo) or (match and rex_match2(s, p, 1 + sx, px, memo)))
                return memo[sx][px]
            else:
                memo[sx][px] = (match and rex_match2(s, p, 1 + sx, 1 + px, memo))
                return memo[sx][px]
        
        return rex_match2(s, p, 0, 0, memo)