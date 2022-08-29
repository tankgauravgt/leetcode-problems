class Solution:
    def hammingWeight(self, n: int) -> int:
        def rec(k):
            if k == 0:
                return 0
            return (k % 2) + rec(k // 2)
        return rec(n)