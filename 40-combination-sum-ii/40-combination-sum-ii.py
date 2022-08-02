from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        rec = dict(Counter(candidates))
        rec = [(n, freq) for n, freq in rec.items()]
        
        res = []
        def btrack(cx, rem, buf):
            nonlocal res
            if rem <= 0:
                if rem == 0:
                    res.append(buf.copy())
                return
            for ix in range(cx, len(rec)):
                n, freq = rec[ix]
                if n <= rem and freq > 0:
                    buf.append(n)
                    rec[ix] = (n, freq - 1)
                    btrack(ix, rem - n, buf)
                    rec[ix] = (n, freq)
                    buf.pop()
        
        btrack(0, target, [])
        return res