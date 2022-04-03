class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        last = None
        groups = []
        
        lx = 0
        rx = 0
        while rx < len(s):
            
            if len(groups) < 1 or s[rx] != last:
                last = s[rx]
                groups += [1]
                lx = rx
                rx = rx + 1
            else:
                groups[-1] = str(int(groups[-1]) + 1)
                last = s[rx]
                rx = rx + 1
        
        counter = 0
        for ix in range(len(groups) - 1):
            counter += min(int(groups[ix]), int(groups[ix+1]))
        
        return counter