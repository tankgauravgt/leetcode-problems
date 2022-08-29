import heapq

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)
        
        l1 = heapq.heappop(nums)
        l2 = heapq.heappop(nums)
        while nums:
            l3 = heapq.heappop(nums)
            if -(l3 + l2) > -l1:
                return -(l1 + l2 + l3)
            else:
                l1, l2 = l2, l3
        
        return 0