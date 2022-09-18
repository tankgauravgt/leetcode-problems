class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        vrec = set()
        def dfs(sx):
            nonlocal vrec
            for nx, n in enumerate(isConnected[sx]):
                if n == 1:
                    if nx not in vrec:
                        vrec.add(nx)
                        dfs(nx)
        
        ctr = 0
        for ix in range(len(isConnected)):
            if ix not in vrec:
                dfs(ix)
                ctr = ctr + 1
        
        return ctr