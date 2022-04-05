class Solution:
                    
    def minDistance(self, word1: str, word2: str) -> int:
        
        res = [[0 for ix in range(1 + len(word1))] for jx in range(1 + len(word2))]
        
        for ix in range(1 + len(word2)):
            res[ix][0] = ix
        
        for jx in range(1 + len(word1)):
            res[0][jx] = jx
        
        for rx in range(len(word2)):
            for cx in range(len(word1)):
                if word1[cx] == word2[rx]:
                    res[1 + rx][1 + cx] = min(1 + res[1 + rx][cx], 1 + res[rx][1 + cx], res[rx][cx])
                else:
                    res[1 + rx][1 + cx] = min(1 + res[1 + rx][cx], 1 + res[rx][1 + cx], 1 + res[rx][cx])
        
        return res[-1][-1]