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
        
        def is_dag(curr):
            nonlocal states
            states[curr] = 'g'
            for adj in G[curr]:
                if states[adj] == 'b':
                    continue
                if states[adj] == 'g':
                    return False
                if not is_dag(adj):
                    return False
            states[curr] = 'b'
            return True
        
        for ix in G:
            if states[ix] == 'w':
                if not is_dag(ix):
                    return []
        
        dq = deque()
        vrec = set()
        for ix in pcount:
            if pcount[ix] == 0:
                dq.append(ix)
                vrec.add(ix)
        
        print(G, pcount)
        
        out = 0
        res = []
        while dq:
            curr = dq.popleft()
            res.append(curr)
            for adj in G[curr]:
                pcount[adj] = pcount[adj] - 1
                if pcount[adj] == 0:
                    dq.append(adj)
                    vrec.add(adj)
        
        return res