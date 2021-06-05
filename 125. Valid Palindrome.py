def isPalindrome(self, s: str) -> bool:
        var="".join(i for i in s if i.isalnum())
        print(var)
        for i in range(len(var)-1,len(var)//2-1,-1):
            if( var[i].lower() != var[len(var)-i-1].lower() ):
                return False
        return True
