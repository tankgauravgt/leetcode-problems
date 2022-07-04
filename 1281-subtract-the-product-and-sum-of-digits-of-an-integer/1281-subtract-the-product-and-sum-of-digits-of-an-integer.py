class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        arr = map(int, str(n))
        
        _sum = 0
        _prod = 1
        for x in arr:
            _sum += x
            _prod *= x
        
        return _prod - _sum