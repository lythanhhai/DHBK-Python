class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        array_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        array_result = []
        for word in words:
            new_morse = ""
            for letter in word:
                new_morse += array_morse[ord(letter) - 97]
            array_result.append(new_morse)
        
        return len(set(array_result))