class Solution:
    
    def __init__(self):
        self.res = []
    
    def generateParenthesis(self, n: int) -> List[str]:
        curr = ""
        self.backtrack(2*n, curr)
        return self.res
    
    
    def backtrack(self, n, current):
        
        # print(f"n: {n}, current: {current}")
        
        if n == 0:
            if self.check(current):
                self.res += [current]
        else:
            self.backtrack(n-1, current + "(")
            self.backtrack(n-1, current + ")")
    
    
    def check(self, s):
        stk = []
        for ix, c in enumerate(s):
            if c == '(':
                stk += [c]
            else:
                if len(stk) == 0 and c == ')':
                    return False
                elif stk[-1] == '(' and c == ')':
                    stk.pop()
                else:
                    stk += [c]
        
        return len(stk) == 0