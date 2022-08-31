class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        for c1, c2 in zip(word1, word2):
            res.append(c1)
            res.append(c2)
        
        if len(word1) > len(word2):
            for c in word1[len(word2)::]:
                res.append(c)
        else:
            for c in word2[len(word1)::]:
                res.append(c)
        
        return "".join(res)