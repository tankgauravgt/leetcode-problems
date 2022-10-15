class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        rec = set(nums)
        
        cmax = 1
        for ix, n in enumerate(nums):
            if n - 1 in rec:
                continue
            
            cnt = 1
            tmp = n
            while tmp + 1 in rec:
                tmp = tmp + 1
                cnt = cnt + 1
            cmax = max(cmax, cnt)
        
        return cmax