class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        nse = [0] * N
        pge = [0] * N
        
        lmax = nums[0]
        rmin = nums[N - 1]
        
        lx = None
        rx = None
        for ix in range(0, N, 1):
            if nums[ix] < lmax:
                rx = ix
            lmax = max(lmax, nums[ix])
        
        for ix in range(N - 1, -1, -1):
            if nums[ix] > rmin:
                lx = ix
            rmin = min(rmin, nums[ix])
        
        if lx == rx == None:
            return 0
        
        return rx - lx + 1