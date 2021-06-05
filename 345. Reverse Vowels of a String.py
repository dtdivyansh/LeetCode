def reverseVowels(self, s: str) -> str:
        s1=[i for i in s]
        i=0
        j=len(s)-1
        while(i < len(s) and i<j):
            if(s1[i] in 'aeiouAEIOU'):
                while(j>=0 and j>i):
                    if(s1[j] in 'aeiouAEIOU'):
                        temp=s1[i]
                        s1[i]=s1[j]
                        s1[j]=temp
                        j-=1
                        break
                    j-=1
            i+=1
            
        return ''.join(s1)
