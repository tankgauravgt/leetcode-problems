import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def rex_match(s, p):
            if not p:
                return not s
            match = (s and p[0] in {s[0], '.'})
            if len(p) > 1 and p[1] == '*':
                return rex_match(s, p[2::]) or (match and rex_match(s[1::], p))
            else:
                return match and rex_match(s[1::], p[1::])
        
        def rex_match2(s, p, sx, px):
            if px == len(p):
                return sx == len(s)
            match = sx < len(s) and p[px] in {s[sx], '.'}
            if px < len(p) - 1 and p[1 + px] == '*':
                return rex_match2(s, p, sx, 2 + px) or (match and rex_match2(s, p, 1 + sx, px))
            else:
                return match and rex_match2(s, p, 1 + sx, 1 + px)
        
        return rex_match2(s, p, 0, 0)