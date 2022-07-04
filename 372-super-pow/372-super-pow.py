class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        b = int("".join(list(map(str, b))))
        
        def dNc(a, b, memo):
            if b < 2:
                return a ** b
            elif b % 2 == 0:
                if b // 2 not in memo:
                    memo[b // 2] = dNc(a, b // 2, memo) % 1337
                return (memo[b // 2] % 1337) * (memo[b // 2] % 1337)
            else:
                if b // 2 not in memo:
                    memo[b // 2] = (dNc(a, b // 2, memo) % 1337)
                return a * (memo[b // 2] % 1337) * (memo[b // 2] % 1337)
        
        return dNc(a, b, {}) % 1337