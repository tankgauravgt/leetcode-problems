class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        cstat = 1
        rstat = 1
        
        nR = len(matrix)
        nC = len(matrix[0])
        
        # column status:
        for cx in range(nC):
            if matrix[0][cx] == 0:
                cstat = 0
        
        # row status:
        for rx in range(nR):
            if matrix[rx][0] == 0:
                rstat = 0
        
        # submatrix status:
        for rx in range(1, nR):
            for cx in range(1, nC):
                if matrix[rx][cx] == 0:
                    matrix[rx][0] = 0
                    matrix[0][cx] = 0
                
        # clear rows:
        for rx in range(1, nR):
            if matrix[rx][0] == 0:
                for cx in range(1, nC):
                    matrix[rx][cx] = 0
        
        # clear columns:
        for cx in range(1, nC):
            if matrix[0][cx] == 0:
                for rx in range(1, len(matrix)):
                    matrix[rx][cx] = 0
        
        if cstat == 0:
            for cx in range(0, nC):
                matrix[0][cx] = 0
        
        if rstat == 0:
            for rx in range(0, nR):
                matrix[rx][0] = 0