class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def findX(row, lx, rx, target):
            if rx >= lx:
                mx = lx + (rx - lx)        
                if matrix[row][mx] < target:
                    return findX(row, mx + 1, rx, target)
                elif matrix[row][mx] > target:
                    return findX(row, lx, mx - 1, target)
                else:
                    return mx
            return -1
            
        for row in range(len(matrix)):
            if target >= matrix[row][0] and target <= matrix[row][-1]:                
                col = findX(row, 0, len(matrix[0]) - 1, target)
                if col != -1:
                    return True
        return False