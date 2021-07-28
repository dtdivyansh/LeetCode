def replaceDigits(self, s: str) -> str:
        
        def shift(x,n):
            a = 'abcdefghijklmnopqrstuvwxyz'
            i = a.index(x)
            return a[i+n]
        
        res = ''
        for i in range(len(s)):
            if(i&1):
                res+=shift(s[i-1],int(s[i]))
            else:
                res+=s[i]
        return res
