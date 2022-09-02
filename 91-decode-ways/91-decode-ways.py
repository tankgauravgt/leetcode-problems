class Solution:
    def numDecodings(self, digits: str) -> int:

        words = {
            str(1 + ix): chr(ord("A") + ix) for ix in range(26)
        }

        memo = {}
        def btrack(sx, mwlen):
            nonlocal memo
            if sx == len(digits):
                return 1

            if sx in memo:
                return memo[sx]

            total = 0
            for ex in range(1 + sx + mwlen, sx, -1):
                if digits[sx:ex] not in words:
                    continue
                else:
                    total = total + btrack(ex, mwlen)
            memo[sx] = total
            return total
                    
        mlen = 2
        return btrack(0, mlen)