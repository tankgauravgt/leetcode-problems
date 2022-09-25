from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        G = {n: [] for n in range(numCourses)}
        for u, v in prerequisites:
            G[v].append(u)
        
        stk = []
        states = {n: 'w' for n in G}
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