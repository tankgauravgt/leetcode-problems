class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ix = 0
        while ix < len(arr):
            if arr[ix] == 0:
                jx = len(arr) - 2
                while jx >= ix + 1:
                    arr[jx + 1] = arr[jx]
                    jx = jx - 1
                if ix < len(arr) - 1:
                    arr[ix + 1] = 0
                ix = ix + 1
            ix = ix + 1