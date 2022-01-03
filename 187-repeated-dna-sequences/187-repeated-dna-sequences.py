class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10:
            return []
        
        rec = {}
        for n in range(len(s) - 9):
            if s[n:n+10] not in rec.keys():
                rec.update({s[n:n+10]: 1})
            else:
                rec[s[n:n+10]] += 1
        
        print(rec)
        
        return list(dict(filter(lambda x: x[1] > 1, rec.items())).keys())