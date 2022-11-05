class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        dp = [0] * len(s)
        
        cmax = 0
        for ix in range(1, len(s)):
            if s[ix - 1] == '(' and s[ix] == ')':
                dp[ix] = 2 + (0 if ix - 2 < 0 else dp[ix - 2])
            elif s[ix - 1] == ')' and s[ix] == ')':
                if ix - 1 - dp[ix - 1] >= 0 and s[ix - 1 - dp[ix - 1]] == '(':
                    dp[ix] = 2 + dp[ix - 1] + (0 if ix - 2 - dp[ix - 1] < 0 else dp[ix - 2 - dp[ix - 1]])
            cmax = max(cmax, dp[ix])
        
        return cmax