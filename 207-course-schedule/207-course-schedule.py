from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G = {ix: [] for ix in range(numCourses)}
        
        for u, v in prerequisites:
            G[u].append(v)
        
        init_nodes = []
        for k, v in G.items():
            if len(v) == 0:
                init_nodes.append(k)
        
        states = {n: 'to_be_visited' for n in G}
        
        def dfs_has_cycle(curr):
            states[curr] = 'visiting'
            
            for adj in G[curr]:
                if states[adj] == 'visited':
                    continue
                if states[adj] == 'visiting':
                    return True
                if dfs_has_cycle(adj):
                    return True
            
            states[curr] = 'visited'
            return False
        
        for inode in G:
            if states[inode] == 'to_be_visited':
                if dfs_has_cycle(inode):
                    return False
        return True