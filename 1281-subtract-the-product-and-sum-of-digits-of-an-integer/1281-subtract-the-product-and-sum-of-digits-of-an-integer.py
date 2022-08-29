class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        temp = list(map(int, str(n)))
        S = sum(temp)
        
        P = 1
        for ix, n in enumerate(temp):
            P *= n
            
        return P - S