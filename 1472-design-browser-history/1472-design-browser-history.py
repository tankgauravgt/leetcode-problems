class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage, None, None)
        self.curr = self.head

    def visit(self, url: str) -> None:
        temp = ListNode(url, self.curr, None)
        self.curr.next = temp
        self.curr = self.curr.next
    
    def back(self, steps: int) -> str:
        while steps:
            if self.curr.prev:
                self.curr = self.curr.prev
            steps = steps - 1
        return self.curr.val
            
    def forward(self, steps: int) -> str:
        while steps:
            if self.curr.next:
                self.curr = self.curr.next
            steps = steps - 1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)