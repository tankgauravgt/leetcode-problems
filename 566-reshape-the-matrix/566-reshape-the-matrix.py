class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if (len(mat) * len(mat[0])) != (r * c):
            return mat
        else:
            new = [[0] * c for _ in range(r)]
            for ix, row in enumerate(mat):
                for jx, n in enumerate(row):
                    loc = ix * len(row) + jx
                    new[loc // c][loc % c] = n    
            return new