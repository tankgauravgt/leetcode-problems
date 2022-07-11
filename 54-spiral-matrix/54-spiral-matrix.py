class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        memo = []
        def print_boundary(sx, ex, sy, ey, count):
            nonlocal memo
            # print(sx, ex, sy, ey)
            if sx < ex and sy < ey:
                if count % 2 == 0:
                    for ix in range(sx, ex):
                        memo.append(matrix[sy][ix])
                    for iy in range(sy + 1, ey):
                        memo.append(matrix[iy][ex - 1])
                    print_boundary(sx, ex - 1, sy + 1, ey, count + 1)
                else:
                    for ix in range(ex - 1, sx - 1, -1):
                        memo.append(matrix[ey - 1][ix])
                    for iy in range(ey - 2, sy - 1, -1):
                        memo.append(matrix[iy][sx])
                    print_boundary(1 + sx, ex, sy, ey - 1, count + 1)
        
        print_boundary(0, len(matrix[0]), 0, len(matrix), 0)
        return memo