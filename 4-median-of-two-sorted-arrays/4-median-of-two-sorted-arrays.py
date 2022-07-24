class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # full length:
        fL = len(nums1) + len(nums2)
        
        # half length:
        hL = fL // 2
        
        def bin_median(lx, rx):
            nonlocal nums1, nums2, hL, fL
            
            mx1 = (rx + lx) // 2
            mx2 = hL - mx1 - 2
            
            a1 = -float('inf') if mx1 < 0 else nums1[mx1]
            a2 = float('inf') if (1 + mx1) >= len(nums1) else nums1[1 + mx1]
            b1 = -float('inf') if mx2 < 0 else nums2[mx2]
            b2 = float('inf') if (1 + mx2) >= len(nums2) else nums2[1 + mx2]
            
            if a1 <= b2 and b1 <= a2:
                if fL % 2 == 1:
                    return min(a2, b2)
                else:
                    return (max(a1, b1) + min(a2, b2)) / 2
            else:
                if a1 > b2:
                    return bin_median(lx, mx1 - 1)
                else:
                    return bin_median(mx1 + 1, rx)
        
        return bin_median(0, len(nums1) - 1)