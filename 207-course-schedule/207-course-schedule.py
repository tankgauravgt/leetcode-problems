from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G = {ix: [] for ix in range(numCourses)}
        for u, v in prerequisites:
            G[u].append(v)
        
        states = {n: 'w' for n in G}
        
        def is_dag(curr):
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
        
        for inode in G:
            if states[inode] == 'w':
                if not is_dag(inode):
                    return False
        return True