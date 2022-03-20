class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for number in range(1, n + 1):
            if number % 3 == 0 and number % 5 == 0:
                res.append("FizzBuzz")
            elif number % 3 == 0:
                res.append("Fizz")
            elif number % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(number))
        return res