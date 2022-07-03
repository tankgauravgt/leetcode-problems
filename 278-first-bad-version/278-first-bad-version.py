# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        def binsearch(lx, rx):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if isBadVersion(mx):
                    lix = binsearch(lx, mx - 1)
                    if lix == -1:
                        return mx
                    else:
                        return lix
                else:
                    return binsearch(mx + 1, rx)
            return -1
        
        return binsearch(1, n)