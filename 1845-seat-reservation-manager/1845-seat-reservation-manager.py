import heapq

class SeatManager:

    def __init__(self, n: int):
        self.hq = [ix for ix in range(1, 1 + n)]

    def reserve(self) -> int:
        return heapq.heappop(self.hq)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hq, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)