def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        values = {}
        for index, letter in enumerate(string.ascii_lowercase):
            values[letter] = index
        
        for word in words:
            morse = ''
            for letter in word:
                morse+=(code[ values[letter] ])
            s.add(morse)
        return len(s)
