class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(1 << len(nums)):
            sset = [nums[j] for j in range(len(nums)) if (i & (1 << j))]
            tmp = 0
            for n in sset:
                tmp ^= n
            res += tmp
        return res