class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for d in range(1, n+1):
            if n % d == 0:
                factors += [d]
        
        if k > len(factors):
            return -1
        
        factors.sort()
        return factors[k-1]