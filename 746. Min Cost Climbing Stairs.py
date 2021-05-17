# Minimum cost climbing stairs

def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for i in range(len(cost)+2)]
        def minCost(cost,n):
            if(dp[n]!=-1):
                return dp[n]
            elif(len(cost)==2):
                dp[n] = cost[n]
                return cost[n]
            elif(n<0):
                dp[n] = 0
                return 0
            elif(n==0):
                dp[n] = cost[n]
                return dp[n]
            else:
                dp[n]= cost[n] + min( minCost(cost,n-1) , minCost(cost,n-2) )
                return dp[n]
        
        return min( minCost(cost,len(cost)-1) , minCost(cost,len(cost)-2) )
