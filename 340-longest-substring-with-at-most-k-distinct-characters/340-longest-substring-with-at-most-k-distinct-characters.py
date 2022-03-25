class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k <= 0:
            return 0

        lx = 0
        rx = 0
        rec = {}
        cmax = 0
        while lx <= rx and rx < len(s):
            
            if len(rec) <= k:
                if s[rx] in rec:
                    rec[s[rx]] = rec[s[rx]] + 1
                else:
                    rec[s[rx]] = 1
                rx = rx + 1
            else:
                while len(rec) > k:
                    if s[lx] in rec:
                        if rec[s[lx]] > 1:
                            rec[s[lx]] = rec[s[lx]] - 1
                        else:
                            rec.pop(s[lx])
                    lx = lx + 1
            if len(rec) <= k:
                cmax = max(cmax, rx - lx)
        
            # print(lx, rx, rec, cmax)
        
        return cmax