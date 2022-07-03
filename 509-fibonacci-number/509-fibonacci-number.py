class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return n
        else:
            pre = 0
            out = 1
            for k in range(n - 1):
                pre, out = out, out + pre
            return out