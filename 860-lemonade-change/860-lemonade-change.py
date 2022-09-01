class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        rec = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            rec[bill] += 1
            diff = (bill - 5)
            while diff > 0:
                if diff >= 20 and rec[20] > 0:
                    diff = diff - 20
                    rec[20] = rec[20] - 1
                elif diff >= 10 and rec[10] > 0:
                    diff = diff - 10
                    rec[10] = rec[10] - 1
                elif diff >= 5 and rec[5] > 0:
                    diff = diff - 5
                    rec[5] = rec[5] - 1
                else:
                    break
            if diff > 0:
                return False
        
        return True