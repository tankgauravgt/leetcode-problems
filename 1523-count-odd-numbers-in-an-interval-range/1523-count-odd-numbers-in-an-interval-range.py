class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low > high: return 0
        
        c1, c2 = low % 2, high % 2
        low, high = low - c1, high + c2
        
        return (high - low) // 2