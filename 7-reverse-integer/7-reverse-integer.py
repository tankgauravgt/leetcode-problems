class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -int(str(x)[1::][::-1])
        else:
            x = +int(str(x)[0::][::-1])  
        return x if x in range(-2**31, 2**31 - 1) else 0