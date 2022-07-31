class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        rec = {}
        def bt(ix, arr):
            nonlocal rec
            if ix >= len(nums):
                if not tuple(sorted(arr)) in rec:
                    rec.update({tuple(sorted(arr)): None})
                return
            
            bt(1 + ix, arr)
            arr.append(nums[ix])
            bt(1 + ix, arr)
            arr.pop()
        
        bt(0, [])
        return list(rec.keys())