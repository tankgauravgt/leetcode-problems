from collections import Counter

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        coordinates.sort(key=lambda x: (x[0], x[1]))
        
        xords = list(map(lambda x: x[0], coordinates))
        xvals = dict(Counter(xords))
        
        yords = list(map(lambda x: x[1], coordinates))
        yvals = dict(Counter(yords))
        
        if len(xvals.keys()) == 1 or len(yvals.keys()) == 1:
            return True
        elif len(xvals.keys()) != len(coordinates) or len(yvals.keys()) != len(coordinates):
            return False
        else:
            l1 = coordinates[0]
            l2 = coordinates[1]

            dy_ref = (l1[1] - l2[1])
            dx_ref = (l1[0] - l2[0])
            for ix in range(2, len(coordinates)):
                l3 = coordinates[ix]
                dy_can = (l2[1] - l3[1])
                dx_can = (l2[0] - l3[0])
                if abs((dy_ref / dx_ref) - (dy_can / dx_can)) > 0.001:
                    return False
                l1, l2 = l2, l3
        return True