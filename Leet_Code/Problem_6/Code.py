class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            string = str(i)
            if '0' in string:
                continue
            count = 0
            for j in string:
                if int(string) % int(j) == 0:
                    count += 1
            if count == len(string):
                res.append(int(string))
                
        return res