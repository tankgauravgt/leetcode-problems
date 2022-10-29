class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def dfs(triangle, rx, cx, memo):
            if rx == len(triangle) - 1:
                return triangle[rx][cx]
            elif (rx, cx) in memo:
                return memo[(rx, cx)]
            lval = triangle[rx][cx] + dfs(triangle, 1 + rx, cx, memo)
            rval = triangle[rx][cx] + dfs(triangle, 1 + rx, 1 + cx, memo)
            memo[(rx, cx)] = min(lval, rval)
            return memo[(rx, cx)]
        
        return dfs(triangle, 0, 0, {})