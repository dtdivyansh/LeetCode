def removePalindromeSub(self, s: str) -> int:
        i,j=0,len(s)-1
        if(j==0):
            return 1
        if(s==s[::-1]):
            return 1
        return 2
