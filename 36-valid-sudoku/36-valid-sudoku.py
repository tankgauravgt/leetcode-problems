class Solution:
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        
        flag = True
        for i in range(9):
            flag = flag and self.verify_row(board, i)
            flag = flag and self.verify_col(board, i)
            flag = flag and self.verify_subbox(board, i)
        return flag
    
    def verify_row(self, board, ix):
        rec = set()
        for j in range(9):
            if board[ix][j] in '123456789':
                if board[ix][j] in rec:
                    return False
                rec = rec | set([board[ix][j]])
            else:
                pass
        return True
    
    
    def verify_col(self, board, jx):
        rec = set()
        for i in range(9):
            if board[i][jx] in '123456789':
                if board[i][jx] in rec:
                    return False
                rec = rec | set([board[i][jx]])
            else:
                pass
        return True
    
    
    def verify_subbox(self, board, ix):

        rx = (ix // 3)
        cx = (ix % 3)
        
        rec = set()
        for r in range(3):
            for c in range(3):
                if board[3*rx+r][3*cx+c] in '123456789':
                    if board[3*rx+r][3*cx+c] in rec:
                        return False
                    rec = rec | set([board[3*rx+r][3*cx+c]])
                else:
                    pass
        return True