class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = 0
        curr = 0
        for ix, n in enumerate(nums):
            if cnt == 0:
                curr = n
            if n == curr:
                cnt = cnt + 1
            else:
                cnt = cnt - 1
        
        return curr