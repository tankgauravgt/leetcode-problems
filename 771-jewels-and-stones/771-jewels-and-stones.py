class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        rec = {}
        count = 0
        for c in stones:
            if c not in rec.keys():
                rec[c] = 1
            else:
                rec[c] += 1
        
        tmp = set(jewels)
        for c in tmp:
            if c in rec:
                count += rec[c]
        return count