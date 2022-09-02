class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        def btrack(sx, buf):
            nonlocal res
            if sx == len(s):
                res.append(buf.copy())
                return
            for ex in range(1 + sx, 1 + len(s)):
                if s[sx:ex] == s[sx:ex][::-1]:
                    buf.append(s[sx:ex])
                    btrack(ex, buf)
                    buf.pop()
        
        btrack(0, [])
        return res