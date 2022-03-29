class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lx = 0
        cx = 0
        rx = len(arr) - 1
        
        while cx <= rx:
            if arr[cx] == 0:
                arr[lx], arr[cx] = arr[cx], arr[lx]
                lx = lx + 1
                cx = cx + 1
            elif arr[cx] == 2:
                arr[rx], arr[cx] = arr[cx], arr[rx]
                rx = rx - 1
            else:
                cx = cx + 1
        
        return arr