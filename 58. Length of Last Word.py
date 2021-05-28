def lengthOfLastWord(self, s: str) -> int:
        l=s.split(" ")
        for i in range(len(l)-1,-1,-1):
            if(l[i].isalpha()):
                return len(l[i])
        return 0
