import heapq

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        heapq.heapify(arr)
        
        A = heapq.heappop(arr)
        B = heapq.heappop(arr)
        
        diff = B - A
        
        while arr:
            A = B
            B = heapq.heappop(arr)
            if (B - A) != diff:
                return False
        return True