class Solution:
    def countAndSay(self, n: int) -> str:
        
        res = str(1)
        
        for i in range(n-1):
            init = res
            record = None
            while init != "":
                if record == None:
                    record = [[1, int(init[0])]]
                else:
                    if record[-1][1] == int(init[0]):
                        record[-1][0] += 1
                    else:
                        record += [[1, int(init[0])]]
                init = init[1::]
            
            
            # preparing result:
            res = ""
            for r in record:
                res += f"{r[0]}{r[1]}"
        
        return res