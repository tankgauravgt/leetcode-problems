class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        A = [[0 for ix in range(n)] for jx in range(n)]
        
        rev = False
        counter = 1
        x_init, x_stop = 0, n - 1
        y_init, y_stop = 0, n - 1
        while x_init <= x_stop or y_init <= y_stop:
            if not rev:
                for ix in range(x_init, 1 + x_stop):
                    A[y_init][ix] = counter
                    counter = counter + 1
                for jx in range(1 + y_init, 1 + y_stop):
                    A[jx][x_stop] = counter
                    counter = counter + 1
                y_init = y_init + 1
                x_stop = x_stop - 1
            else:
                for ix in range(x_stop, x_init - 1, -1):
                    A[y_stop][ix] = counter
                    counter = counter + 1
                for jx in range(y_stop - 1, y_init - 1, -1):
                    A[jx][x_init] = counter
                    counter = counter + 1
                y_stop = y_stop - 1
                x_init = x_init + 1
            rev = not rev
        
        return A