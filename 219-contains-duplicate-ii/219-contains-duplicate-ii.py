class Solution:
    def containsNearbyDuplicate(self, nums, k):
        rec = {}
        for kx, vx in enumerate(nums):
            if vx in rec and kx - rec[vx] <= k:
                return True
            rec[vx] = kx
        return False