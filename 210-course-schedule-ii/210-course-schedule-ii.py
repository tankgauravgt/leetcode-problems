from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = {n: [] for n in range(numCourses)}
        for u, v in prerequisites:
            G[v].append(u)
        
        pcount = {n: 0 for n in G}
        for u, v in G.items():
            for c in v:
                pcount[c] += 1
        
        states = {n: 'w' for n in G}
        
        stk = []
        def is_dag(curr):
            nonlocal states, stk
            states[curr] = 'g'
            for adj in G[curr]:
                if states[adj] == 'b':
                    continue
                if states[adj] == 'g':
                    return False
                if not is_dag(adj):
                    return False
            stk.append(curr)
            states[curr] = 'b'
            return True
        
        for ix in G:
            if states[ix] == 'w':
                if not is_dag(ix):
                    return []
        
        res = []
        while stk:
            res.append(stk.pop())
        
        return res