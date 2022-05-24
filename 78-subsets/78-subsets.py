class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for ix in range(1 << len(nums)):
            tmp = []
            for bx in range(len(nums)):
                if ix & (1 << bx):
                    tmp += [nums[bx]]
            res += [tmp]
        return res