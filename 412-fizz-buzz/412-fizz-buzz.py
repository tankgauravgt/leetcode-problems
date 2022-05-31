class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for ix in range(1, n+1):
            out = ''
            if ix % 3 == 0:
                out += 'Fizz'
            if ix % 5 == 0:
                out += 'Buzz'
            if out == '':
                answer.append(str(ix))
            else:
                answer.append(out)
        return answer