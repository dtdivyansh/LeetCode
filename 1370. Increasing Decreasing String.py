def sortString(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        count = {}
        for i in alpha:
            count[i]=0
        for i in s:
            count[i]+=1
        res = ''
        n=len(s)
        size = 0
        while(size!=n):
            for i in alpha:
                if( count[i]!=0 ):
                    res+=i
                    size+=1
                    count[i]-=1
            for i in range(25,-1,-1):
                if( count[alpha[i]]!=0 ):
                    res+=alpha[i]
                    size+=1
                    count[alpha[i]]-=1
        return res
