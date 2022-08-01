class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def rec(ix, rem, arr):
            nonlocal ans
            if ix == len(candidates):
                if rem == 0:
                    ans.append(arr.copy())
                return
            
            if candidates[ix] <= rem:
                arr.append(candidates[ix])
                rec(ix, rem - candidates[ix], arr)
                arr.pop()
            rec(1 + ix, rem, arr)
        
        rec(0, target, [])
        return ans