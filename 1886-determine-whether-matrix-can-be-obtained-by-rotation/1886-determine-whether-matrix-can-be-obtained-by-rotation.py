class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        R, C = len(mat), len(mat[0])
        
        def compare(m1, m2):
            for ix in range(R):
                for jx in range(C):
                    if mat[ix][jx] != target[ix][jx]:
                        return False
            return True
        
        def rotate(mat):
            for jx in range(C):
                for ix in range(1 + jx, R):
                    mat[ix][jx], mat[jx][ix] = mat[jx][ix], mat[ix][jx]
            for rx, row in enumerate(mat):
                mat[rx] = row[::-1]
        
        for ix in range(4):
            if compare(mat, target):
                return True
            else:
                rotate(mat)
        return False