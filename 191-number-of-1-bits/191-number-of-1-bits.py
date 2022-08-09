class Solution:
    def hammingWeight(self, n: int) -> int:
        def dnc(k):
            if k == 0:
                return 0
            return (k % 2) + dnc(k // 2)
        return dnc(n)