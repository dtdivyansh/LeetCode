# Minimum Cost for tickets

def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def cost(day,costs,j,p):
            if((j,p) in dp.keys()):
                return dp[(j,p)]
            if(j>=len(day)):
                dp[(j,p)] = 0
                return 0
            elif(day[j]==0):
                j = day[j:].index(1) + len(day[:j])
                dp[(j,p)] = min( cost(day,costs,j,0), cost(day,costs,j,1), cost(day,costs,j,2))
                return dp[(j,p)]
            elif(day[j]==1):
                if(p==0):
                    d = 1
                elif(p==1):
                    d = 7
                else:
                    d = 30
                t1 = costs[p] + min(cost(day,costs,j+d,0), cost(day,costs,j+d,1), cost(day,costs,j+d,2))
                dp[(j,p)] = t1
                return t1   
            
        day = []
        for i in range(max(days)+1):
            if(i not in days):
                day.append(0)
            else:
                day.append(1)
        j=1
        out = min( cost(day,costs,j,0), cost(day,costs,j,1), cost(day,costs,j,2))
        return out
