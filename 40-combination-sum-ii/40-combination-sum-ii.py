from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        rec = dict(Counter(candidates))
        rec = [(n, freq) for n, freq in rec.items()]
        
        def btrack(cx, rem, buf):
            nonlocal res
            if rem <= 0:
                if rem == 0:
                    res.append(buf.copy())
                return
            for ix in range(cx, len(rec)):
                if rec[ix][0] <= rem:
                    val, freq = rec[ix]
                    if freq > 0:
                        buf.append(val)
                        rec[ix] = (val, freq - 1)
                        btrack(ix, rem - val, buf)
                        rec[ix] = (val, freq)
                        buf.pop()
        
        btrack(0, target, [])
        return res