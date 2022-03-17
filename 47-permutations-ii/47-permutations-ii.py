class Solution:
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        current = []
        self.backtrack(nums, current, result)
        return set(result)
    
    
    def backtrack(self, remaining, current, result):
        if len(remaining) == 0:
            result += [tuple(current)]
            return
        
        for ix in range(len(remaining)):
            remaining[0], remaining[ix] = remaining[ix], remaining[0]
            current_copy = current + [remaining[0]]
            self.backtrack(remaining[1::], current_copy, result)
            remaining[0], remaining[ix] = remaining[ix], remaining[0]