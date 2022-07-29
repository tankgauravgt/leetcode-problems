class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stk = [(-1, '$')]
        for ix, c in enumerate(s):
            if stk and c == ')' and stk[-1][1] == '(':
                stk.pop()
            else:
                stk.append((ix, c))
        
        stk.append((len(s), '$'))
        
        longest = 0
        for ix in range(len(stk) - 1):
            longest = max(longest, stk[1 + ix][0] - stk[ix][0] - 1)
        
        return longest