class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x / y)
        }
        
        stk = []
        for tok in tokens:
            if tok in ops:
                v2 = stk.pop()
                v1 = stk.pop()
                stk.append(int(ops[tok](v1, v2)))
            else:
                stk.append(int(tok))
        
        return stk[0]