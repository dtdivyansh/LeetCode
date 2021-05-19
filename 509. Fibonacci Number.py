def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        
        def fibo(n):
            if(dp[n]!=(-1)):
                return dp[n]
            
            elif(n<2):
                dp[n] = n
                return dp[n]
            
            else:
                dp[n] = fibo(n-1)+fibo(n-2)
                return dp[n]
            
        return fibo(n)
