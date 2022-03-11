class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        count = 0 # số từ trong sentence
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", "U"]
        arr = sentence.split(" ")
        arr_res = []
        for index in range(0, len(arr)):
            res = ""
            if arr[index][0] in vowel:
                res += arr[index] + "ma"
                for i in range(0, index + 1):
                    res += "a"
                arr_res.append(res)
            else:
                for i in range(1, len(arr[index])):
                    res += arr[index][i]
                res += arr[index][0] + "ma"
                for i in range(0, index + 1):
                    res += "a"
                arr_res.append(res)
        result = ""
        for i in range(0, len(arr_res)):
            if i == len(arr_res) - 1:
                result += arr_res[i]
            else:
                result += arr_res[i] + " "
        return result