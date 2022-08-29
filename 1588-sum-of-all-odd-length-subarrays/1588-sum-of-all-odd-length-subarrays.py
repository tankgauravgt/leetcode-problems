class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        res = 0
        for win in range(1, 1 + len(arr), 2):
            for ix in range(len(arr) - win + 1):
                res += sum(arr[ix:ix+win])
        return res