class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " " + s.rstrip(" ")
        for ix, c in enumerate(s[::-1]):
            if c == " ":
                return ix
        return 0