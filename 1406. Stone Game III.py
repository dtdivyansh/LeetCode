def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [None for i in range(50001)]
        
        def solve(arr,i):
            if(dp[i]!=None):
                return dp[i]
            if(i>=len(arr)):
                return 0
            else:
                ans = -100000007
                val=0
                for j in range(3):
                    if(i+j >= len(arr)):
                        break
                    else:
                        val+=arr[i+j]
                        ans = max(ans, val-solve(arr,i+j+1))
                dp[i]=ans        
                return dp[i]
        
        res = solve(stoneValue,0)
        
        if(res>0):
            return 'Alice'
        elif(res==0):
            return 'Tie'
        else:
            return 'Bob'
