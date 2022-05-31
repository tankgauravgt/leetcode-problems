class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        lx = 0
        rx = 0
        out = 0
        for ix, c in enumerate(s):
            if c == 'L':
                lx = lx + 1
            if c == 'R':
                rx = rx + 1
            if lx == rx:
                out = out + 1
        
        return out