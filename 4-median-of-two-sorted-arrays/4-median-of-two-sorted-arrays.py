class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_len = len(nums1) + len(nums2)
        half_len = final_len//2
        if len(nums1) > len(nums2): A, B = nums2, nums1
        else: A, B = nums1, nums2
        left, right = 0, len(A)-1
        while True:
            midA = (left + right)//2
            midB = half_len - midA - 2
            
            left_A = A[midA] if midA >= 0 else float("-infinity")
            right_A = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            
            left_B = B[midB] if midB >= 0 else float("-infinity")
            right_B = B[midB + 1] if (midB + 1) < len(B) else float("infinity")
            
            if left_A <= right_B  and left_B <= right_A:
                if final_len % 2:
                    return min(right_A, right_B)
                else: return (max(left_A, left_B) + min(right_A, right_B)) / 2
            elif left_A > right_B: right = midA - 1
            else: left = midA + 1