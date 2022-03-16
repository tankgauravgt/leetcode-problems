import re

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_str = []
        t_str = []
        
        for c in s:
            if c == '#':
                if len(s_str) > 0:
                    s_str.pop()
            else:
                s_str += [c]
        
        for c in t:
            if c == '#':
                if len(t_str) > 0:
                    t_str.pop()
            else:
                t_str += [c]
        
        return s_str == t_str