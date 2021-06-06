def findLUSlength(self, a: str, b: str) -> int:
        m=0
        if(len(a) < len(b)):
            return len(b)
        if(len(a) > len(b)):
            return len(a)
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if( a[i:j+1] not in b and j-i+1 > m):
                    m= j-i+1
        if(m==0):
            return -1
        return m
