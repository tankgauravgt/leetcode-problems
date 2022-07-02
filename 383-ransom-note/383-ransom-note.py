from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def check(value, true):
            for k, v in value.items():
                if k not in true or true[k] < v:
                    return False
            return True
        
        true = dict(Counter(magazine))
        value = dict(Counter(ransomNote))
        
        return check(value, true)