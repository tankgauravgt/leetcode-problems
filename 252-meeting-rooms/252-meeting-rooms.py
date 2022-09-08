import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key=lambda x: x[0])
        
        hq = []
        max_rooms = 0
        for sx, ex in intervals:
            while hq and hq[0] <= sx:
                heapq.heappop(hq)
            heapq.heappush(hq, ex)
            max_rooms = max(max_rooms, len(hq))
        
        if max_rooms < 2:
            return True
        return False