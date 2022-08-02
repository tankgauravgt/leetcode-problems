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
                if rec[ix][1] > 0:
                    buf.append(rec[ix][0])
                    rec[ix] = (rec[ix][0], rec[ix][1] - 1)
                    btrack(ix, rem - rec[ix][0], buf)
                    rec[ix] = (rec[ix][0], rec[ix][1] + 1)
                    buf.pop()
        
        btrack(0, target, [])
        return res