class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        nge = [-1 for n in nums]
        
        nums = nums * 2
        
        stk = []
        for nx, n in enumerate(nums):
            while stk and stk[-1][1] < n:
                ix, val = stk.pop()
                nge[ix % (len(nums) // 2)] = n
            stk.append([nx, n])
        
        return nge