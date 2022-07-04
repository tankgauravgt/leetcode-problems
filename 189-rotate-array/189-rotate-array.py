class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums)
        
        if k > N:
            k = k % N
            
        for ix in range(N // 2):
            nums[ix], nums[N - ix - 1] = nums[N - ix - 1], nums[ix]
        
        for ix in range(k // 2):
            nums[ix], nums[k - ix - 1] = nums[k - ix - 1], nums[ix]
        
        for ix in range((N - k) // 2):
            nums[k + ix], nums[N - ix - 1] = nums[N - ix - 1], nums[k + ix]
        
        return nums