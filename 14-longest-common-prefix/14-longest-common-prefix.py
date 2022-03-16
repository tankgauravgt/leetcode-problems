class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        temp = list(zip(*strs))
        
        if temp == []:
            return ""
        else:
            tx = 0
            while tx < len(temp):
                if len(set(temp[tx])) == 1:
                    tx = tx + 1
                else:
                    break
            return strs[0][0:tx]