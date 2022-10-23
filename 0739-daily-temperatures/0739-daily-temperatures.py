class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stk = []
        for ix, n in enumerate(temperatures):
            while stk and stk[-1][1] < n:
                jx, val = stk.pop()
                ans[jx] = ix - jx
            stk.append((ix, n))
        return ans