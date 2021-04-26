# Climbing Stairs DP

def climbStairs(self, n: int) -> int:
        dp = {}
        
        def climb(n):
            if(n in dp.keys()):
                return dp[n]
            
            if(n<=1):
                dp[n]=1
                return 1
            elif(n==2):
                dp[n] = 2
                return 2
            
            else:
                dp[n] = climb(n-2)+climb(n-1)
                return dp[n]
            
        return climb(n)
