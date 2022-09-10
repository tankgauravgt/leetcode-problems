class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        
        res = []
        def rec(sx, buf, maxlen):
            if sx == len(s):
                res.append(" ".join(buf))
            for ex in range(1 + sx, min(1 + sx + maxlen, 1 + len(s))):
                if s[sx:ex] in wordDict:
                    buf.append(s[sx:ex])
                    rec(ex, buf, maxlen)
                    buf.pop()
            
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
            
        rec(0, [], maxlen)
        return res