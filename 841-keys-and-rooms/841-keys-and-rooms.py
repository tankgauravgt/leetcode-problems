from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        G = {ix: arr for ix, arr in enumerate(rooms)}
        
        dq = deque([0])
        vrec = set([0])
        
        while dq:
            curr = dq.popleft()
            for adj in G[curr]:
                if adj not in vrec:
                    vrec.add(adj)
                    dq.append(adj)
        
        return len(vrec) == len(rooms)