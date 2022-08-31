class Solution:
    def freqAlphabets(self, s: str) -> str:
        lx = 0
        res = []
        while lx < len(s):
            if s[lx:lx+3][-1] == "#":
                res.append(s[lx:lx + 2])
                lx = lx + 3
            else:
                res.append(s[lx])
                lx = lx + 1
        
        res = list(map(lambda x: chr(int(x) + ord("a") - 1), res))
        
        return "".join(res)