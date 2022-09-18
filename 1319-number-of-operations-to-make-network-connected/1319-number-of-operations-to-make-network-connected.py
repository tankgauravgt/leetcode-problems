class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        e = len(connections)
        
        if e < (n - 1):
            return -1
        
        G = {ix: set() for ix in range(n)}

        for u, v in connections:
            G[u].add(v)
            G[v].add(u)
        
        vrec = set()
        def dfs(curr_node):
            nonlocal vrec
            for next_node in G[curr_node]:
                if next_node not in vrec:
                    vrec.add(next_node)
                    dfs(next_node)
        
        cnt = 0
        for start_node in G:
            if start_node not in vrec:
                dfs(start_node)
                cnt = cnt + 1
        
        return cnt - 1