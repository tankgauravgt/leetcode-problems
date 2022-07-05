class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        cmin_id = -1
        cmin = float('inf')
        
        for ix, pt in enumerate(points):
            if pt[0] == x or pt[1] == y:
                dist = abs(pt[0] - x) + abs(pt[1] - y)
                if cmin > dist:
                    cmin = dist
                    cmin_id = ix
        
        return cmin_id