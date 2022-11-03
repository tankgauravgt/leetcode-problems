class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def re_match(s, p, sx, px, memo):
            if px == len(p):
                return sx == len(s)
            if (sx, px) in memo:
                return memo[(sx, px)]
            match = (sx < len(s) and p[px] in {'?', '*', s[sx]})
            if p[px] == '*':
                memo[(sx, px)] = (re_match(s, p, sx, 1 + px, memo) or (match and re_match(s, p, 1 + sx, px, memo)))
                return memo[(sx, px)]
            else:
                memo[(sx, px)] = (match and re_match(s, p, 1 + sx, 1 + px, memo))
                return memo[(sx, px)]
        
        memo = {}
        res = re_match(s, p, 0, 0, memo)
        return res