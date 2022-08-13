class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        nR = len(board)
        nC = len(board[0])
        
        def isValid(rid, cid, num):
            nonlocal board, nR, nC
            for ix in range(nR):
                if board[ix][cid] == num:
                    return False
                if board[rid][ix] == num:
                    return False
                bir, bic = (rid // 3), (cid // 3)
                if board[(3 * bir) + (ix // 3)][(3 * bic) + (ix % 3)] == num:
                    return False
            return True
        
        
        def backtrack(sr, sc):
            nonlocal board, nR, nC
            for rx in range(sr, nR):
                for cx in range(nC):
                    if board[rx][cx] == '.':
                        for n in range(1, 10):
                            if isValid(rx, cx, str(n)):
                                board[rx][cx] = str(n)
                                if backtrack(sr, sc):
                                    return True
                                else:
                                    board[rx][cx] = '.'
                        return False
            return True
        
        backtrack(0, 0)