class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)
        string = ""
        res = 0
        for i in range(2, len(binary)):
            if binary[i] == "0":
                string += "1"
            else:
                string += "0"
        string =  string[::-1]
        for i in range(0, len(string)):
            if string[i] == "1":
                res += pow(2, i)
           
        return res
        