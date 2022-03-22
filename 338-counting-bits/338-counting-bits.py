from collections import Counter

class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for num in range(n+1):
            rec = dict(Counter(str(bin(num))))
            out += [rec.get("1", 0)]
        return out