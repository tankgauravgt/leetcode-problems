class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for ix in range(len(nums)):
            rec.update({nums[ix]: ix})
        
        for ix in range(len(nums)):
            if (target - nums[ix]) in rec.keys():
                if rec[target - nums[ix]] != ix:
                    return [ix, rec[target - nums[ix]]]
                
        return None