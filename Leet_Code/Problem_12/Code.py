class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        index = 0
        for element in s.split(" "):
            if index == len(s.split(" ")) - 1:
                res += element[::-1]
            else:
                res += element[::-1] + " "
            index += 1
        return res
        
        