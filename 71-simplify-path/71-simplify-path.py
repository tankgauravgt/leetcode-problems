class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stk = []
        for px in path.split("/"):
            if px == "":
                continue
            elif px == ".":
                continue
            elif px == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(px)
        
        return "/" + "/".join(stk)