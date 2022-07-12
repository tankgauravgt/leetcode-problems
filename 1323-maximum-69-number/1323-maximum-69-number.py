class Solution:
    def maximum69Number (self, num: int) -> int:
        
        id6 = str(num).find('6')
        if id6 != -1:
            return str(num)[:id6] + '9' + str(num)[1 + id6::]
        return num