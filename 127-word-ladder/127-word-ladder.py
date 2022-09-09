from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordset = set(wordList)
        
        rec = set([beginWord])
        def get_neighbors(word):
            neighbors = []
            temp = list(word)
            for ix in range(len(word)):
                for c in range(ord('a'), 1 + ord('z')):
                    x = temp[ix]
                    temp[ix] = chr(c)
                    candidate = "".join(temp)
                    if candidate in wordset and candidate not in rec:
                        neighbors.append("".join(temp))
                    temp[ix] = x
            return neighbors
        
        count = 1
        dq = deque([beginWord])
        while dq:
            N = len(dq)
            for ix in range(N):
                temp = dq.popleft()
                if temp == endWord:
                    return count
                for adj in get_neighbors(temp):
                    rec.add(adj)
                    dq.append(adj)
            count = count + 1
        
        return 0