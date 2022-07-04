class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        lx = m - 1
        rx = n - 1
        while lx >= 0 and rx >= 0:
            if nums1[lx] <= nums2[rx]:
                nums1[lx + rx + 1] = nums2[rx]
                rx = rx - 1
            else:
                nums1[lx + rx + 1] = nums1[lx]
                lx = lx - 1
                
        while lx >= 0:
            nums1[lx + rx + 1] = nums1[lx]
            lx = lx - 1
        
        while rx >= 0:
            nums1[lx + rx + 1] = nums2[rx]
            rx = rx - 1