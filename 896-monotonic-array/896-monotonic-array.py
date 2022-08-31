class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        is_dec, is_inc = True, True
        
        last = nums[0]
        for n in nums[1::]:
            if n < last:
                is_inc = False
            if n > last:
                is_dec = False
            if not is_inc and not is_dec:
                return False
            last = n
        
        return True