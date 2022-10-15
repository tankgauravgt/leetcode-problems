import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x: x[0])
        
        def overlap(l1, l2):
            return min(l1[1], l2[1]) - max(l1[0], l2[0]) > 0
        
        for ix in range(1, len(intervals)):
            if overlap(intervals[ix - 1], intervals[ix]):
                return False
        return True