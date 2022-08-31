class Solution:
    def toLowerCase(self, s: str) -> str:
        
        rec = {chr(ord("A") + ix):chr(ord("a") + ix) for ix in range(26)}
        
        res = []
        for ix, c in enumerate(s):
            if ord(c) in range(ord("A"), 1 + ord("Z")):
                res.append(rec[c])
            else:
                res.append(c)
        
        return "".join(res)