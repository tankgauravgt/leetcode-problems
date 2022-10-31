class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        mat = [[float('inf')] * n for ix in range(n)]
        
        for ix in range(n):
            mat[ix][ix] = 0
            
        for ix, jx, weight in edges:
            mat[ix][jx] = weight
            mat[jx][ix] = weight
        
        for kx in range(n):
            for ix in range(n):
                for jx in range(n):
                    mat[ix][jx] = min(mat[ix][jx], mat[ix][kx] + mat[kx][jx])
        
        target = 0
        accessible = float('inf')
        for ix, arr in enumerate(mat):
            curr = len(list(filter(lambda x: x <= distanceThreshold, arr)))
            if accessible >= curr:
                accessible = curr
                target = ix                
        return target