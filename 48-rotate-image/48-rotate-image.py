class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = matrix        
        N = len(matrix)
        
        for rx in range((1 + N) // 2):
            for cx in range(N // 2):
                m[rx][cx], m[N-cx-1][rx], m[N-rx-1][N-cx-1], m[cx][N-rx-1] = m[N-cx-1][rx], m[N-rx-1][N-cx-1], m[cx][N-rx-1], m[rx][cx]