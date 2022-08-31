class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def is_arithmatic(arr):
            if len(arr) == 1:
                return True
            diff = arr[1] - arr[0]
            for ix in range(len(arr) - 1):
                if diff != (arr[ix + 1] - arr[ix]):
                    return False
            return True
        
        res = []
        for sx, ex in zip(l, r):
            arr = sorted(nums[sx:1 + ex])
            res.append(is_arithmatic(arr))
        
        return res