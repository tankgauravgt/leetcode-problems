class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle) > 1:
            for d in range(len(triangle) - 2, -1, -1):
                for ix in range(len(triangle[d])):
                    triangle[d][ix] = triangle[d][ix] + min(triangle[1 + d][ix], triangle[1 + d][1 + ix])
        
        return triangle[0][0]