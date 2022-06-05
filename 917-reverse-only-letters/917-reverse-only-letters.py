class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        s = list(s)
        
        lx = 0
        rx = len(s) - 1
        rec = set('abcdefghijklmnopqrstuvwxyz') | set('abcdefghijklmnopqrstuvwxyz'.upper())
        
        while lx < rx:
            if s[lx] not in rec:
                lx = lx + 1
            if s[rx] not in rec:
                rx = rx - 1
            if s[lx] in rec and s[rx] in rec:
                s[lx], s[rx] = s[rx], s[lx]
                lx = lx + 1
                rx = rx - 1
        
        return "".join(s)