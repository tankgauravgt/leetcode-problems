import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:        
        
        k = k - 1
        buf = [(1 + ix) for ix in range(n)]
        
        out = []
        while len(buf):
            sg_size = math.factorial(n - 1 - len(out))
            ix = k // sg_size
            out.append(buf[ix])
            buf.pop(ix)
            k = k % sg_size
        
        return "".join(list(map(str, out)))