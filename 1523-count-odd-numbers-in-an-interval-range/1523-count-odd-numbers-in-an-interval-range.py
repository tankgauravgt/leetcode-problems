class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return 0 if low % 2 == 0 else 1
        else:
            if high % 2 == 0:
                high = high - 1
            return 1 + (high - low) // 2