def halvesAreAlike(self, s: str) -> bool:
        c1 = 0
        n = len(s)//2
        vowels = set(['a','A','e','E','o','O','i','I','u','U'])
        
        for i in range(n*2):
            if( s[i] in vowels ):
                if(i<n):
                    c1+=1
                else:
                    c1-=1
        
        if(c1):
            return False
        return True
