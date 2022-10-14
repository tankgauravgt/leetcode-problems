class DSets:
    
    def __init__(self):
        self.rec = {}
    
    def union(self, x, y):
        self.rec[self.find(y)] = self.find(x)
    
    def find(self, x):
        y = self.rec.get(x, x)
        if y != x:
            self.rec[x] = y = self.find(y)
        return y    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        rec = DSets()
        
        ans = []
        for u, v in edges:
            if rec.find(u) == rec.find(v):
                ans = [u, v]
            rec.union(u, v)
            
        return ans