import random

class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        elif len(self.data) == 1:
            self.data = []
            self.idx = {}
            return True
        else:
            last = self.data[-1]
            self.idx[last] = self.idx[val]
            self.data[self.idx[val]] = last
            self.idx.pop(val)
            self.data.pop()
            return True
            
    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()