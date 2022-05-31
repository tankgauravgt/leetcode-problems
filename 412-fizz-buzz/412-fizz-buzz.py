class Solution:
    
    def fizzBuzz(self, n: int) -> List[str]:
        
        def func(k):
            if (k % 3) and (k % 5):
                return str(k)
            elif (k % 3 == 0) and (k % 5 == 0):
                return 'FizzBuzz'
            elif (k % 3 == 0) and (k % 5):
                return 'Fizz'
            else:
                return 'Buzz'
        
        return list(map(lambda x: func(x), range(1, n+1)))