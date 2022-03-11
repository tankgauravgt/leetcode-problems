class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # sum of first k elements:
        c_sum = sum(nums[0:k])
        
        # avg of first k elements:
        m_avg = c_sum / k
         
        # finding same for remaining:
        for ix in range(k, len(nums), 1):
            c_sum = c_sum - nums[ix-k] + nums[ix]
            if (c_sum / k) > m_avg:
                m_avg = (c_sum / k)
        
        # return maximum average:
        return m_avg