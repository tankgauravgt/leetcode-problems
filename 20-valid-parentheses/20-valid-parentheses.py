class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ix, c in enumerate(s):
            if c in '({[':
                stk += [c]
            else:
                if len(stk) == 0:
                    return False
                else:
                    if c == ')' and stk[-1] == '(':
                        stk.pop()
                    elif c == '}' and stk[-1] == '{':
                        stk.pop()
                    elif c == ']' and stk[-1] == '[':
                        stk.pop()
                    else:
                        return False
        return len(stk) == 0