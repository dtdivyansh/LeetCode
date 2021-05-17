# palindromic Substrings

def countSubstrings(self, s: str) -> int:
        def lpsPrint(s,n):
            dp = [[0 for j in range(n)] for i in range(n)]
            c=0
            for i in range(n):
                dp[i][i]=1
                c+=1
            for i in range(n-1):
                if(s[i]==s[i+1]):
                    dp[i][i+1]=1
                    c+=1
                    
            for i in range(n-1,-1,-1):
                for j in range(i+2,n):
                    if(s[i]==s[j] and dp[i+1][j-1]):
                        dp[i][j]= 1
                        c+=1
                    else:
                        dp[i][j] = 0
                        
            return c
        
        return lpsPrint(s,len(s))
