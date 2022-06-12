class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        def recurse(arr, buf, k):
            if k == len(arr):
                tmp = 0
                nonlocal res
                for n in buf:
                    tmp = (tmp ^ n)
                res = res + tmp
                return
            buf.append(nums[k])
            recurse(arr, buf, k + 1)
            buf.pop()
            recurse(arr, buf, k + 1)
        
        recurse(nums, [], 0)
        return res