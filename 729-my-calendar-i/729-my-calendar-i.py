class MyCalendar:

    def __init__(self):
        self.bookings = set()

    def book(self, start: int, end: int) -> bool:
        for booking in self.bookings:
            if start in booking:
                return False
            if booking.start in range(start, end):
                return False
        self.bookings.add(range(start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)