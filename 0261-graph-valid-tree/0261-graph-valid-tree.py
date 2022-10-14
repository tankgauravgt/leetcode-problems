class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        rec = {}
        
        def find(rec, x):
            y = rec.get(x, x)
            if y != x:
                rec[x] = y = find(rec, y)
            return y
        
        def union(rec, x, y):
            rec[find(rec, y)] = find(rec, x)
        
        for u, v in edges:
            if find(rec, u) != find(rec, v):
                union(rec, u, v)
                continue
            return False
        
        temp = set()
        for ix in range(n):
            temp.add(find(rec, ix))
        
        return len(temp) == 1