class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = 0
        c = 1
        for ix in range(len(digits) - 1, -1, -1):
            s = c + digits[ix]
            c = s // 10
            s = s % 10
            digits[ix] = s
        
        if c != 0:
            return [c] + digits
        return digits