class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        n1 = num
        n2 = [int(c) for c in str(k)]
        
        p1 = len(n1) - 1
        p2 = len(n2) - 1
        
        c = 0
        s = 0
        res = []
        while p1 >= 0 and p2 >= 0:
            s = (c + n1[p1] + n2[p2]) % 10
            c = (c + n1[p1] + n2[p2]) // 10
            res.append(s)
            p1 = p1 - 1
            p2 = p2 - 1
            
        while p1 >= 0:
            s = (c + n1[p1]) % 10
            c = (c + n1[p1]) // 10
            res.append(s)
            p1 = p1 - 1
            
        while p2 >= 0:
            s = (c + n2[p2]) % 10
            c = (c + n2[p2]) // 10
            res.append(s)
            p2 = p2 - 1
            
        if c != 0:
            res.append(c)
            
        return res[::-1]