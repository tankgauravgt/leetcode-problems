class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lx = 0
        current = 0
        record = set()
        
        for rx, c in enumerate(s):
            if c not in record:
                record = record | set([c])
                current = max(current, rx - lx + 1)
            else:
                while s[lx] != c:
                    record.remove(s[lx])
                    lx = lx + 1
                lx = lx + 1
        
        return current