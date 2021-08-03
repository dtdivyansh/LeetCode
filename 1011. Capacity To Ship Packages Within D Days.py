def shipWithinDays(self, weights: List[int], D: int) -> int:
        def fun(weights,d,k,n):
            v=0
            for i in range(n):
                if(v+weights[i]<k):
                    v+=weights[i]
                elif(v+weights[i]==k):
                    d-=1
                    v=0
                else:
                    d-=1
                    v=weights[i]
                if(d<0):
                    return False
                
            if((d>0 and v) or v==0):
                return True
            else:
                return False
                
                    
        s = sum(weights)
        n = len(weights)
        #p = max(s//D,max(weights))
        p = max(weights)
        k=0
        while(p<s):
            k = (p+s)//2
            g = fun(weights,D,k,n)
            if(g):
                s = k
            else:
                p = k+1
        return s
