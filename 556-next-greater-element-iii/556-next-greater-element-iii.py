class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        arr = [int(c) for c in str(n)]
        
        lx = len(arr) - 2
        while lx >= 0 and arr[lx + 1] <= arr[lx]:
            lx = lx - 1    
        
        if lx == -1:
            return -1
        
        rx = 1 + lx
        cmax = [rx, arr[rx]]
        while rx < len(arr):
            if arr[rx] <= cmax[1] and arr[rx] > arr[lx]:
                cmax = [rx, arr[rx]]
            rx = rx + 1
        arr[lx], arr[cmax[0]] = cmax[1], arr[lx]
        arr[1 + lx::] = sorted(arr[1 + lx::])
        
        num = int("".join([str(n) for n in arr]))
        
        if -(2 ** 31) <= num <= ((2 ** 31) - 1):
            return num
        else:
            return -1