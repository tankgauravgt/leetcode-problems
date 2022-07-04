class Solution:
    def hammingWeight(self, n: int) -> int:
        def dnc(k):
            return 0 if k == 0 else 1 + dnc(k & (k - 1))
        return dnc(n)