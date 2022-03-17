class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = list(mapping[digits[0]])
        
        print(res)
        
        for dx, d in enumerate(digits[1::]):
            res = [old + new for old in res for new in mapping[d]]
        
        return res