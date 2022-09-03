class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        npops = 1
        while self.stk and self.stk[-1][0] <= price:
            val, n = self.stk.pop()
            npops += n
        self.stk.append((price, npops))
        return self.stk[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)