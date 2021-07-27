def reverseWords(self, s: str) -> str:
        s = [i for i in s]
        i,j=0,0
        l = len(s)
        
        while(j<l):
            if(j==l-1 or s[j+1]==' '):
                k = j
                while(i<j):
                    s[i],s[j] = s[j],s[i]
                    i+=1
                    j-=1
                i = k+2
                j = k+2
            else:
                j+=1
                
        return ''.join(s)
