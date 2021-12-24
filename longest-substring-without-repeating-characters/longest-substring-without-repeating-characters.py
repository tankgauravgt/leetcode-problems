class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lx = 0
        cmax = 0
        hist = set()
        
        for rx, c in enumerate(s):
            if c not in hist:
                cmax = max(cmax, rx-lx+1)
                hist = hist | set(c)
            else:
                while s[lx] != c:
                    hist.remove(s[lx])
                    lx = lx + 1
                lx = lx + 1
        
        return cmax