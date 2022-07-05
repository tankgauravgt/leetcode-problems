import heapq

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums = [-n for n in nums]
        
        heapq.heapify(nums)
        
        n3 = heapq.heappop(nums)
        n2 = heapq.heappop(nums)
        n1 = heapq.heappop(nums)
        
        if n1 + n2 < n3:
            return -(n1 + n2 + n3)
        
        while nums:
            n3 = n2
            n2 = n1
            n1 = heapq.heappop(nums)
            if n1 + n2 < n3:
                return -(n1 + n2 + n3)
        
        return 0