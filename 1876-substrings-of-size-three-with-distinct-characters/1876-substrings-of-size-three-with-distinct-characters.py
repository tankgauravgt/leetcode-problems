class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for ix in range(len(s) - 2):
            if len(set(s[ix:ix+3])) == 3:
                count = count + 1
        return count