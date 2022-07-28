class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        buf = ['']
        for k in range(n):
            res = []
            for c in buf:
                res.append('0' + c)
            for c in buf[::-1]:
                res.append('1' + c)
            buf = res
        
        return list(map(lambda x: int(x, 2), buf))