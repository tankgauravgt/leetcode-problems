class Solution:
    def maximum69Number (self, num: int) -> int:
        tmp = list(str(num))
        if '6' in tmp:
            id6 = tmp.index('6')
            tmp[id6] = '9'
            return int("".join(tmp))
        return num