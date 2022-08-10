class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        found = False
        def btrack(ix, jx, px, word):
            nonlocal found
            if px == len(word):
                found = True
                return
            if ix < 0 or ix >= len(board): return
            if jx < 0 or jx >= len(board[0]): return
            if board[ix][jx] == word[px]:
                board[ix][jx] = '.'
                btrack(ix + 1, jx, 1 + px, word)
                if found: return
                btrack(ix - 1, jx, 1 + px, word)
                if found: return
                btrack(ix, jx + 1, 1 + px, word)
                if found: return
                btrack(ix, jx - 1, 1 + px, word)
                if found: return
                board[ix][jx] = word[px]
            else:
                return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    btrack(i, j, 0, word)
        
        return found