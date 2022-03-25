class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        lx = 0
        rx = 0
        rec = {}
        cmax = 0
        while lx <= rx  and rx < len(fruits):
            if len(rec) <= 2:
                if fruits[rx] in rec:
                    rec[fruits[rx]] += 1
                else:
                    rec[fruits[rx]] = 1
                rx = rx + 1
            else:
                while len(rec) > 2:
                    if fruits[lx] in rec:
                        if rec[fruits[lx]] > 1:
                            rec[fruits[lx]] -= 1
                        else:
                            rec.pop(fruits[lx])
                    lx = lx + 1
            
            if len(rec) <= 2:
                cmax = max(cmax, rx - lx)
        
        return cmax