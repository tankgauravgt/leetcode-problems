class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        wait = [0] * len(temperatures)
        
        stk = []
        for ix, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                rec = stk.pop()
                wait[rec[1]] = ix - rec[1]
            stk.append((temp, ix))
        
        return wait