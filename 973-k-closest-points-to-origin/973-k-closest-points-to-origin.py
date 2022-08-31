import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = list(map(lambda x: ((x[0] ** 2) + (x[1] ** 2), x), points))
        heapq.heapify(dist)
        
        res = []
        for ix in range(k):
            res.append(heapq.heappop(dist)[1])
        return res