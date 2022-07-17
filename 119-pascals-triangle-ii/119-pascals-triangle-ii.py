class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        rec = []
        for rx in range(1 + rowIndex):
            temp = []
            for cx in range(1 + rx):
                if cx < 1 or cx >= rx:
                    temp.append(1)
                else:
                    temp.append(rec[cx - 1] + rec[cx])
            rec = temp
        
        return rec