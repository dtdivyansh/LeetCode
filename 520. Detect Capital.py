def detectCapitalUse(self, word: str) -> bool:
        if(word.isupper()):
            return True
        if(word.islower()):
            return True
        k=0
        for i in word:
            if(i.isupper() and k!=0):
                return False
            k+=1
        return True
