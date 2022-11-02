import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        dp = [[float('inf'), float('inf')]] * (1 + len(envelopes))
        dp[0] = [-float('inf'), -float('inf')]
                
        def rbinsearch(arr, lx, rx, target):
            while rx >= lx:
                mid = lx + (rx - lx) // 2
                if arr[mid][0] < target[0] and arr[mid][1] < target[1]:
                    return rbinsearch(arr, mid + 1, rx, target)
                else:
                    return rbinsearch(arr, lx, mid - 1, target)
            return lx
        
        cmax = 0
        for ix, n in enumerate(envelopes):
            jx = rbinsearch(dp, 0, len(dp) - 1, n)
            dp[jx] = n
            cmax = max(cmax, jx)
        return cmax