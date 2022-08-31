class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = [-1] * len(nums1)
        rec = {n:ix for ix, n in enumerate(nums1)}
        
        stk = []
        for ix, n in enumerate(nums2):
            while stk and stk[-1] < n:
                val = stk.pop()
                if val in rec:
                    res[rec[val]] = n
            stk.append(n)
        
        return res