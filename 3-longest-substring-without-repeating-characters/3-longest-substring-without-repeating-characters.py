class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lx = 0
        c_max = 0
        rec = set()
        
        for rx, c in enumerate(s):
            
            if c not in rec:
                rec = rec | set([c])
                c_max = max(c_max, rx - lx + 1)
            else:
                while c != s[lx]:
                    rec.remove(s[lx])
                    lx = lx + 1
                lx = lx + 1
                
        return c_max
