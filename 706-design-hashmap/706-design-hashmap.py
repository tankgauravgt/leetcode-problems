class ListNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

        
class Bucket:
    
    def __init__(self):
        self.head = None
    
    
    def insert(self, k, v):
        if self.retrieve(k) == -1:
            self.head = ListNode(k, v, self.head)
        else:
            tx = self.head
            while tx:
                if tx.key == k:
                    tx.val = v
                    break
                tx = tx.next
    
    
    def retrieve(self, k):
        tx = self.head
        while tx:
            if tx.key == k:
                return tx.val
            tx = tx.next
        return -1

    
    def delete(self, k):
        if self.head == None:
            return
        
        if self.head and self.head.key == k:
            self.head = self.head.next
            return
            
        tx = self.head
        while tx and tx.next and tx.next.key != k:
            tx = tx.next
        if tx and tx.next and tx.next.key == k:
            tx.next = tx.next.next
            return
    
        
class MyHashMap:

    def __init__(self):
        self.rec = []
        for ix in range(1000):
            self.rec += [Bucket()]

    def put(self, key: int, value: int) -> None:
        self.rec[key % 1000].insert(key, value)

    def get(self, key: int) -> int:
        return self.rec[key % 1000].retrieve(key)

    def remove(self, key: int) -> None:
        self.rec[key % 1000].delete(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)