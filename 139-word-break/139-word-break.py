class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        max_wlen = len(max(wordDict, key=lambda x: len(x)))
        
        memo = {}
        def btrack(s, sx):
            nonlocal max_wlen, memo
            if sx == len(s):
                return True
            elif sx in memo:
                return memo[sx]
            else:
                found = False
                for ex in range(1 + sx, 1 + sx + max_wlen):
                    if ex <= len(s) and s[sx:ex] in wordDict:
                        if s[sx:ex] not in memo:
                            memo[ex] = btrack(s, ex)
                        found = found or memo[ex]
                memo[sx] = found
                return memo[sx]
                
        return btrack(s, 0)