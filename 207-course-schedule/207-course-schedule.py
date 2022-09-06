from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G = {n: [] for n in range(numCourses)}
        for u, v in prerequisites:
            G[u].append(v)
        
        pc = {n: 0 for n in G}
        for u, v in prerequisites:
            pc[v] = pc[v] + 1
        
        fringe = deque()
        for n in G:
            if pc[n] == 0:
                fringe.append(n)
        
        count = 0
        while fringe:
            temp = fringe.popleft()
            for adj in G[temp]:
                pc[adj] = pc[adj] - 1
                if pc[adj] == 0:
                    fringe.append(adj)
            count = count + 1
        
        return len(G) == count