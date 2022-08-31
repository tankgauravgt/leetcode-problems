class Solution:
    def interpret(self, command: str) -> str:
        
        lx = 0
        res = []
        while lx < len(command):
            if command[lx:lx+4] == "(al)":
                res.append("al")
                lx = lx + 4
            elif command[lx:lx+2] == "()":
                res.append("o")
                lx = lx + 2
            else:
                res.append("G")
                lx = lx + 1
        
        return "".join(res)