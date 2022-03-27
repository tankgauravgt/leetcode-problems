class Solution:
    
    def required(self, d1, d2):
        for k in d2:
            if (d2[k] - d1[k]) > 0:
                return True
        return False
    
    
    def minWindow(self, str1: str, pattern: str) -> str:

        if len(str1) < len(pattern):
            return ""
            
        rec = dict(Counter(pattern))

        lx = 0
        rx = 0
        cstr= ""
        cmin = float('inf')
        
        rec = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz'.lower()}
        crec = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'.upper() + 'abcdefghijklmnopqrstuvwxyz'.lower()}

        for c in pattern:
            rec[c] += 1
        
        while lx <= rx and rx < len(str1):
            
            if self.required(crec, rec) == False:
                if rx - lx < cmin:
                    cmin = min(cmin, rx - lx)
                    cstr = str1[lx:rx]
                crec[str1[lx]] -= 1
                lx = lx + 1
            else:
                crec[str1[rx]] += 1
                rx = rx + 1

        while self.required(crec, rec) == False:
            if rx - lx < cmin:
                cmin = min(cmin, rx - lx)
                cstr = str1[lx:rx]
            crec[str1[lx]] -= 1
            lx = lx + 1

        return cstr