import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        N = len(nums)
        
        hq = []
        res = []
        for ix in range(N):
            if ix < k - 1:
                heapq.heappush(hq, (-nums[ix], ix))
                continue
            heapq.heappush(hq, (-nums[ix], ix))
            while ix - hq[0][1] >= k:
                heapq.heappop(hq)
            res.append(-hq[0][0])
        
        return res