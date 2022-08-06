import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        insert_ix = bisect.bisect_left(intervals, newInterval[0], 0, len(intervals), key=lambda x: x[0])
        intervals = intervals[0:insert_ix] + [newInterval] + intervals[insert_ix::]
        
        res = []
        last = intervals[0]
        for curr in intervals[1::]:
            if curr[0] < last[1] and curr[1] <= last[1]:
                continue
            elif curr[0] <= last[1] and curr[1] >= last[1]:
                last[1] = curr[1]
            else:
                res.append(last)
                last = curr
        res.append(last)
        
        return res