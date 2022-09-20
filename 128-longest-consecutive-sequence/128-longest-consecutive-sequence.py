class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        rec = set(nums)
        
        max_len = 0
        for n in nums:
            if n - 1 not in rec:
                cnum = n
                clen = 1
                while cnum + 1 in rec:
                    cnum = cnum + 1
                    clen = clen + 1
                max_len = max(clen, max_len)
        
        return max_len