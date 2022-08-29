class Solution:
    def arraySign(self, nums: List[int]) -> int:
        P = 1
        for ix, n in enumerate(nums):
            P *= n
        
        if P == 0:
            return 0
        elif P < 0:
            return -1
        else:
            return 1