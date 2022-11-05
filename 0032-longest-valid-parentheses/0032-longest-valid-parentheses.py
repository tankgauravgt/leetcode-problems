class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        dp = [0] * len(s)
        
        cmax = 0
        for ix, c in enumerate(s):
            if c == ')':
                if ix - 1 >= 0 and s[ix - 1] == '(':
                    dp[ix] = 2 + (0 if ix < 2 else dp[ix - 2])
                elif ix - dp[ix - 1] - 1 >= 0 and s[ix - 1 - dp[ix - 1]] == '(':
                    dp[ix] = 2 + dp[ix - 1] + (0 if ix - dp[ix - 1] < 2 else dp[ix - dp[ix - 1] - 2])
                cmax = max(cmax, dp[ix])
        
        return cmax