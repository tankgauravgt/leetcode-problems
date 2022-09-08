class DLL:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.rec = {}
        self.size = 0
        self.head = DLL(None, None)
        self.tail = DLL(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    
    def remove_node(self, node):
        px = node.prev
        nx = node.next
        px.next = nx
        nx.prev = px
    
    def insert_node(self, key, value):
        node = DLL(key, value)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        return node
    
    def get(self, key: int) -> int:
        if key not in self.rec:
            return -1
        val = self.rec[key].val
        self.remove_node(self.rec[key])
        self.rec[key] = self.insert_node(key, val)
        return self.rec[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.rec:
            self.remove_node(self.rec[key])
            self.rec[key] = self.insert_node(key, value)
        elif self.size < self.capacity:
            self.rec[key] = self.insert_node(key, value)
            self.size = self.size + 1
        else:
            self.rec.pop(self.head.next.key)
            self.remove_node(self.head.next)
            self.rec[key] = self.insert_node(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)