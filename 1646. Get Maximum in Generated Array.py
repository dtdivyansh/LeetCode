def getMaximumGenerated(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1 or n==2):
            return 1
        
        num = [-1 for i in range(n+1)]
        num[0],num[1]=0,1
        m = 0
        
        for i in range(2,n+1):
            if(i&1):
                num[i] = num[i//2] + num[i//2+1]
            else:
                num[i] = num[i//2]
            m = max(m,num[i])
        return m
