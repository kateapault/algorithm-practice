class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # set up morse code hash map
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        alphamorse = {}
        for i in range(0,26):
            alphamorse[alphabet[i]] = morse[i]
        
        morse_words = {}
        for word in words:
            morse_word =''
            for letter in word:
                morse_word += alphamorse[letter]
            if morse_word in morse_words:
                morse_words[morse_word] += 1
            else:
                morse_words[morse_word] = 1
        return len(morse_words)