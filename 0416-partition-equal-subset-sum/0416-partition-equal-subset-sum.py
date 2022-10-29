class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        
        if target % 2:
            return False
        
        def dfs(nums, ix, csum, target, memo):
            if csum == target:
                return True
            elif csum > target:
                return False
            elif ix == len(nums):
                return False
            elif (ix, csum) in memo:
                return memo[(ix, csum)]
            flag = False
            flag = flag or dfs(nums, 1 + ix, csum, target, memo)
            if not flag:
                flag = flag or dfs(nums, 1 + ix, csum + nums[ix], target, memo)
            memo[(ix, csum)] = flag
            return flag

        return dfs(tuple(nums), 0, 0, target // 2, {})