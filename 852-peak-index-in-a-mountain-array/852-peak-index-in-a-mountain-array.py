class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def binsearch(arr, lx, rx):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if arr[mx] < arr[mx + 1]:
                    return binsearch(arr, mx + 1, rx)
                else:
                    return binsearch(arr, lx, mx - 1)
            return lx
        
        return binsearch(arr, 0, len(arr) - 1)