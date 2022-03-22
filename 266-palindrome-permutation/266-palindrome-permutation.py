from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        # print(list(filter(lambda x: x % 2, dict(Counter(s)).values())))
        
        if len(s) % 2 == 0:
            return len(list(filter(lambda x: x % 2, dict(Counter(s)).values()))) == 0
        else:
            return len(list(filter(lambda x: x % 2, dict(Counter(s)).values()))) == 1