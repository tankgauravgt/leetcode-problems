class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def rec(ix, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            for jx in range(ix, 1 + n):
                arr.append(jx)
                rec(1 + jx, arr)
                arr.pop()
        
        rec(1, [])
        return res