def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        for i in range(1,len(sequence)//len(word)+1):
            if(word*i in sequence):
                c+=1
            else:
                break
        return c
