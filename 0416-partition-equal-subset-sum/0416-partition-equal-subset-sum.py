class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        if target % 2:
            return False
        
        buf = [[False for jx in range(1 + (target // 2))], None]
        buf[0][0] = True
        
        for rx, n in enumerate(nums):
            prev = None
            curr = None
            if rx % 2 == 0:
                prev = buf[0]
                buf[1] = curr = prev.copy()
            else:
                prev = buf[1]
                buf[0] = curr = prev.copy()
            
            for sx in range(1 + target // 2):
                if prev[sx] == True:
                    if sx + n in range(0, 1 + (target // 2)):
                        curr[sx + n] = True
                        
            if curr[target // 2]:
                return True
        
        return False