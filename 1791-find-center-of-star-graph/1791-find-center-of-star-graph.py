class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for n in set(edges[0]) & set(edges[1]):
            return n