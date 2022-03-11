class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        
        # sum for first k values:
        c_sum = sum(calories[0:k])

        # assigning points for first k days:
        c_pts = 0
        if c_sum < lower:
            c_pts = c_pts - 1
        if c_sum > upper:
            c_pts = c_pts + 1
        
        # moving window starting from element 2:
        for ix in range(k, len(calories), 1):
            c_sum = c_sum - calories[ix - k] + calories[ix]
            if c_sum < lower:
                c_pts = c_pts - 1
            if c_sum > upper:
                c_pts = c_pts + 1
        
        return c_pts