class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        rec = {}
        for s in strs:
            if str(sorted(s)) not in rec:
                rec[str(sorted(s))] = [s]
            else:
                rec[str(sorted(s))] += [s]
        return list(map(lambda lst: list(lst), rec.values()))