from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        res = []
        for item in words:
            temp = []
            r1 = 0
            r2 = 0
            r3 = 0
            count = 0
            for element in item:
                if element.lower() in firstRow:
                    r1 += 1
                elif element.lower() in secondRow:
                    r2 += 1
                else:
                    r3 += 1
            temp.append(r1)
            temp.append(r2)
            temp.append(r3)
            for i in temp:
                if i > 0:
                    count += 1
            if count > 1:
                continue
            else:
                res.append(item)
        return res
            
print(Solution().findWords(["qwee"]))