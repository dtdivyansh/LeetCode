def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        text = text.split()
        for w in text:
            for i in brokenLetters:
                if(i in w):
                    c-=1
                    break
            c+=1
        return c
