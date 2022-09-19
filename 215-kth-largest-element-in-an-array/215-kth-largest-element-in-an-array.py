import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        
        heapq.heapify(nums)
        
        last = 0
        for ix in range(k):
            last = -heapq.heappop(nums)
        return last