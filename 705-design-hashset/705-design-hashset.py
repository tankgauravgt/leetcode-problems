class ListNode:
    
    def __init__(self, val, next):
        self.val = val
        self.next = next    

        
class Bucket:
    
    def __init__(self):
        self.head = None
            
    def insert(self, val):
        if not self.contains(val):
            self.head = ListNode(val, self.head)
        
    def contains(self, val):
        tx = self.head
        while tx:
            if tx.val == val:
                return True
            tx = tx.next
        return False
    
        
    def delete(self, val):
        if self.head == None:
            return
        
        if self.head and (not self.head.next) and self.head.val == val:
            self.head = None
            return

        tx = self.head
        while tx and tx.next and tx.next.val != val:
            tx = tx.next
        
        if tx and tx.next and tx.next.val == val:
            tx.next = tx.next.next
    

class MyHashSet:

    def __init__(self):
        self.rec = []
        for ix in range(100000):
            self.rec += [Bucket()]
            
    def add(self, key: int) -> None:
        self.rec[key % 100000].insert(key)
        return

    def remove(self, key: int) -> None:
        self.rec[key % 100000].delete(key)
        return
        
    def contains(self, key: int) -> bool:
        return self.rec[key % 100000].contains(key)
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)