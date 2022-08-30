from collections import Counter

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for ix in range(len(coordinates) - 2):
            p1, p2, p3 = coordinates[ix:ix+3]
            if (p3[1] - p2[1]) * (p2[0] - p1[0]) != (p2[1] - p1[1]) * (p3[0] - p2[0]):
                return False
        return True
