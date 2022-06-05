class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        s = list(s)
        
        lx = 0
        rx = len(s) - 1
        
        rec_a = set(range(ord('A'), 1 + ord('Z')))
        rec_b = set(range(ord('a'), 1 + ord('z')))
        rec = rec_a | rec_b
        
        while lx < rx:
            if ord(s[lx]) not in rec:
                lx = lx + 1
            if ord(s[rx]) not in rec:
                rx = rx - 1
            if ord(s[lx]) in rec and ord(s[rx]) in rec:
                s[lx], s[rx] = s[rx], s[lx]
                lx = lx + 1
                rx = rx - 1
        
        return "".join(s)