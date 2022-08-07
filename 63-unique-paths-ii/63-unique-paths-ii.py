class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        nR = len(obstacleGrid)
        nC = len(obstacleGrid[0])
        
        temp = obstacleGrid[0][0]
                
        rx_found = False
        for rx in range(nR):
            if obstacleGrid[rx][0] == 1:
                obstacleGrid[rx][0] = 0
                rx_found = True
                continue
            obstacleGrid[rx][0] = 1 if not rx_found else 0
                
        cx_found = False
        for cx in range(nC):
            if cx == 0:
                if temp == 1:
                    cx_found = True
                continue
            if obstacleGrid[0][cx] == 1:
                obstacleGrid[0][cx] = 0
                cx_found = True
                continue
            obstacleGrid[0][cx] = 1 if not cx_found else 0
        
        
        for rx in range(1, nR):
            for cx in range(1, nC):
                if obstacleGrid[rx][cx] == 1:
                    obstacleGrid[rx][cx] = 0
                    continue
                obstacleGrid[rx][cx] = obstacleGrid[rx - 1][cx] + obstacleGrid[rx][cx - 1]
        
        return obstacleGrid[nR - 1][nC - 1]