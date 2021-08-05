#  WITHOUT DP SLOW
def getKth(self, lo: int, hi: int, k: int) -> int:
        def fun(n):
            if(n==1):
                return 0
            else:
                c=0
                while(n!=1):
                    if(n&1):
                        n = n*3+1
                    else:
                        n = n//2
                    c+=1
                return c
                    
        ans = []
        for i in range(lo,hi+1):
            ans.append([i,fun(i)])
        
        ans.sort(key=lambda x:x[1])
        #print(ans)
        return ans[k-1][0]

      
# WITH DP FAST
def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = {}
        def fun(n):
            nonlocal arr
            if(n in arr.keys()):
                return arr[n]
            
            if(n==1):
                return 0
            else:
                if(n&1):
                    a = 1 + fun(3*n+1)
                else:
                    a = 1 + fun(n//2)
                arr[n] = a
                return a
            
        ans = []
        for i in range(lo,hi+1):
            ans.append([i,fun(i)])
        
        ans.sort(key=lambda x:x[1])
        #print(ans)
        return ans[k-1][0]
