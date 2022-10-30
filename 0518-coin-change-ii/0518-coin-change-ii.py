class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        buf = [0] * (1 + amount)
        buf[0] = 1

        for coin in coins:
            for sx in range(coin, 1 + amount):
                buf[sx] = buf[sx] + buf[sx - coin]

        return buf[amount]