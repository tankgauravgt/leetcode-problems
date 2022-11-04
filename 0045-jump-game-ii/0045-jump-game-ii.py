from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:

        dq = deque([0])
        vrec = set([0])
        
        cnt = 0
        while dq:
            mix = dq[-1]
            N = len(dq)
            for ix in range(N):
                curr = dq.popleft()
                if curr == len(nums) - 1:
                    return cnt
                for adj in range(mix, 1 + curr + nums[curr]):
                    if adj not in vrec:
                        vrec.add(adj)
                        dq.append(adj)
            cnt = cnt + 1
        
        return -1