class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        fwd_cost = [cost[0], cost[1]]
        for ix in range(2, len(cost), 1):
            fwd_cost.append(min(fwd_cost[ix - 1], fwd_cost[ix - 2]) + cost[ix])
            
        return min(fwd_cost[-1], fwd_cost[-2])