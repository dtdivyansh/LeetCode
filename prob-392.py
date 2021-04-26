 # Is subsequence
 
 def isSubsequence(self, s: str, t: str) -> bool:
        def printLCS(a,b,m,n):   # DP Aproach
            dp2 = [[0 for i in range(n+1)] for j in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if( b[j-1] == a[i-1] ):
                        dp2[i][j] = 1 + dp2[i-1][j-1]
                    else:
                        dp2[i][j] = max( dp2[i-1][j],dp2[i][j-1] )
            return dp2[m][n]               
        #l = printLCS(s,t,len(s),len(t))
        #return l==len(s)
        
        if(len(s)==0 ):  # Stack aproach  (FASTER THAN DP)
            return True
        if(len(t)==0):
            return False
        a = [i for i in s]
        a.append(0)
        for j in t:
            if(j==a[0]):
                a.pop(0)
        if(len(a)==1):
            return True
        else:
            return False
