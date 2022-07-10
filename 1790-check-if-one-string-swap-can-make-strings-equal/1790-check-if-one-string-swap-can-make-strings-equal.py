class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        rec = []
        for ix, c in enumerate(zip(s1, s2)):
            if c[0] != c[1]:
                rec += [ix]
        
        if not rec:
            return True
        elif len(rec) == 2:
            arr1 = list(s1)
            arr2 = list(s2)
            arr2[rec[0]], arr2[rec[1]] = arr2[rec[1]], arr2[rec[0]]
            if "".join(arr1) != "".join(arr2):
                arr2[rec[0]], arr2[rec[1]] = arr2[rec[1]], arr2[rec[0]]
                return "".join(arr1) == "".join(arr2)
            else:
                return True
        else:
            return False