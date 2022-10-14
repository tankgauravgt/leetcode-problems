class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        nR = len(board)
        nC = len(board[0])
        
        vrec = set()
        def dfs(rx, cx):
            nonlocal board, vrec
            
            vrec.add((rx, cx))
            board[rx][cx] = 'T'
            
            for rr, cc in [(rx, cx - 1), (rx, cx + 1), (rx - 1, cx), (rx + 1, cx)]:
                if rr in range(0, nR) and cc in range(0, nC):
                    if (rr, cc) not in vrec and board[rr][cc] == 'O':
                        dfs(rr, cc)
        
        for cx in range(nC):
            if board[0][cx] == 'O':
                dfs(0, cx)
            if board[nR - 1][cx] == 'O':
                dfs(nR - 1, cx)
        
        for rx in range(nR):
            if board[rx][0] == 'O':
                dfs(rx, 0)
            if board[rx][nC - 1] == 'O':
                dfs(rx, nC - 1)
        
        for rx in range(nR):
            for cx in range(nC):
                if board[rx][cx] == 'O':
                    board[rx][cx] = 'X'
        
        for rx in range(nR):
            for cx in range(nC):
                if board[rx][cx] == 'T':
                    board[rx][cx] = 'O'