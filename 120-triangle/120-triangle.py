class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        def dp(d):
            nonlocal triangle
            if d < 0:
                return
            for ix in range(1 + d):
                triangle[d][ix] = triangle[d][ix] + min(triangle[1 + d][ix], triangle[1 + d][1 + ix])
            dp(d - 1)
        
        dp(len(triangle) - 2)
        return triangle[0][0]