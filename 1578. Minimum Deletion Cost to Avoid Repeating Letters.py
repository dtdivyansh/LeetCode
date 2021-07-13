def minCost(self, s: str, cost: List[int]) -> int:
        l = len(s)
        c,size = 0,1
        top = s[0]
        m=cost[0]
        total = cost[0]
        for i in range(1,l):
            if(top==s[i]):
                m = max(m,cost[i])
                total = total+cost[i]
                size+=1
            else:
                if(size>1):
                    c = total-m + c
                    size = 1
                total = cost[i]
                m = cost[i]
                top = s[i]
        if(size>1):
            c = total-m + c
        
        return c
