def longestPalindrome(self, s: str) -> str:
        if(len(s)==1):
            return s
        def pali(s,i,j):
            while(i>=0 and j<len(s) and s[i]==s[j]):
                i-=1
                j+=1
            return s[i+1:j]
        
        v = ''
        for i in range(len(s)):
            v = max( pali(s,i,i) , pali(s,i,i+1),v,key=len )
        return v
