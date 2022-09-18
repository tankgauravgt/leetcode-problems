class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        G = {ix: [] for ix in range(n)}
        
        for ix, mx in enumerate(manager):
            if mx != -1:
                G[mx].append(ix)
        
        vrec = set()
        def dfs(curr_node, total_time):
            nonlocal vrec
            total_time = informTime[curr_node]
            max_time = 0
            for next_node in G[curr_node]:
                if next_node not in vrec:
                    vrec.add(next_node)
                    max_time = max(max_time, dfs(next_node, 0))            
            return total_time + max_time
        
        return dfs(headID, 0)