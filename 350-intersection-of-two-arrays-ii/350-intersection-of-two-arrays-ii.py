from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        rec1 = dict(Counter(nums1))
        rec2 = dict(Counter(nums2))
        
        out = []
        for k in (rec1 | rec2):
            if k in rec1 and k in rec2:
                out.extend([k] * min(rec1[k], rec2[k]))
        return out