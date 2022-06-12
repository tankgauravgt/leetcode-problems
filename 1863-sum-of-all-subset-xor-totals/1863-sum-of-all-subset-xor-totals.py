class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        buf = []
        def recurse(arr, k):
            nonlocal buf, res
            if k == len(arr):
                tmp = 0
                for n in buf:
                    tmp = (tmp ^ n)
                res = res + tmp
                return
            buf.append(nums[k])
            recurse(arr, k + 1)
            buf.pop()
            recurse(arr, k + 1)
        
        recurse(nums, 0)
        return res