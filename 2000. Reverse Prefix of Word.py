def reversePrefix(self, word: str, ch: str) -> str:
        i=0
        j=0
        s = [k for k in word]
        l = len(s)
        flag=False
        while(i<=j and j<l):
            if(s[j]!=ch and flag==False):
                j+=1
            else:
                flag=True
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        
        return ''.join(s)
