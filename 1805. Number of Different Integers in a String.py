def numDifferentIntegers(self, word: str) -> int:
        set1 = set()
        n = ''
        for i in word:
            if(i.isdigit()):
                n+=i
            else:
                if(n!=''):
                    set1.add(int(n))
                    n=''
        if(n!=''):
            set1.add(int(n))
        
        return len(set1)
