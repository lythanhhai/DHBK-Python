import math
class Solution:
    def checkPrime(number):
        if number < 2:
            return False
        elif number == 2 or number == 3:
            return True
        else:
            for item in range(2, int(math.sqrt(number)) + 1):
                if number % item == 0:
                    return False
            return True
    def Count(number):
        count = 0
        for i in number:
            if i == '1':
                count += 1
        return count
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            temp = "{0:b}".format(i)
            print(temp)
            if Solution.checkPrime(Solution.Count(str(temp))) == True:
                count += 1
        return count

a = Solution()

print(a.countPrimeSetBits(10, 15))
    