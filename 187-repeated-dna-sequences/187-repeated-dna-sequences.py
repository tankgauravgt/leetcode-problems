class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 11:
            return []
        
        rec = {}
        for ix in range(len(s) - 10 + 1):
            if s[ix:ix + 10] not in rec:
                rec[s[ix:ix+10]] = 1
            else:
                rec[s[ix:ix+10]] = rec[s[ix:ix+10]] + 1
        
        out = []
        for candidate in filter(lambda x: x[1] > 1, rec.items()):
            if candidate:
                out += [candidate[0]]
        
        return out