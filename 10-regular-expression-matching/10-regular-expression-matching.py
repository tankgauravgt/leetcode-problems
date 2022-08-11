import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.match(p, s)
        if res and res.span() == (0, len(s)):
            return True
        return False