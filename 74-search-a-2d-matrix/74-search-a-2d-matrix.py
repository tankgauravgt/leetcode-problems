class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def findY(uy, dy, target):
            if dy >= uy:
                my = uy + (dy - uy) // 2
                if matrix[my][0] <= target and matrix[my][-1] >= target:
                    return my
                elif my > 0 and matrix[my - 1][-1] >= target:
                    return findY(uy, my - 1, target)
                else:
                    return findY(my + 1, dy, target)
            return -1
        
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
            
        row = findY(0, len(matrix) - 1, target)
        
        if row != -1:
            col = findX(row, 0, len(matrix[0]) - 1, target)
            if col != -1:
                return True
        
        return False