import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        insert_ix = bisect.bisect_left(intervals, newInterval[0], 0, len(intervals), key=lambda x: x[0])
        intervals = intervals[0:insert_ix] + [newInterval] + intervals[insert_ix::]
        
        # [1, 3], [2, 5], [6, 9]
        # ======================================
        # ix = 0, lx = 0: [1, 3]
        # ix = 1, lx = 0: [1, 5], [2, 5],
        # ix = 2, lx = 0: [1, 5], [2, 5], [6, 9]
        
        
        lx = 0
        for ix, curr in enumerate(intervals):
            if ix == 0:
                continue
            if intervals[lx][1] >= curr[0] and intervals[lx][1] < curr[1]:
                intervals[lx][1] = curr[1]
            elif intervals[lx][1] < curr[0]:
                lx = lx + 1
                intervals[lx] = curr
            else:
                continue
        
        return intervals[0:1 + lx]