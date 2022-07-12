class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(cap):
            lx = 0
            for jx in range(days):
                curr = 0
                while lx < len(weights) and curr <= cap:
                    if curr + weights[lx] <= cap:
                        curr += weights[lx]
                        lx = lx + 1
                    else:
                        break
                if lx >= len(weights):
                    break
            return (lx >= len(weights))
        
        def binsearch(lx, rx):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if feasible(mx):
                    tx = binsearch(lx, mx - 1)
                    if tx != -1:
                        return tx
                    return mx
                else:
                    return binsearch(mx + 1, rx)
            return -1
        
        return binsearch(weights[-1], sum(weights))