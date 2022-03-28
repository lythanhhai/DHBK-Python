class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = "{0:b}".format(n)
        count = 0
        for i in range(0, len(temp) - 1):
            if temp[i] != temp[i + 1]:
                count += 1
        if count == len(temp) - 1:
            return True
        else:
            return False
        