class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digits = list(filter(lambda x: x.split()[1].isnumeric(), logs))
        non_digits = list(filter(lambda x: not x.split()[1].isnumeric(), logs))         
        non_digits.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return non_digits + digits