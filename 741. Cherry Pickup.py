def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = {}
        
        def go(grid,r1,c1,c2,n):
                r2 = r1+c1-c2
                if((r1,c1,c2) in dp.keys()):
                    return dp[(r1,c1,c2)]
                
                if(c1>n or c2>n):
                    return -10000007
                if(r1>n or r2>n):
                    return -10000007
                if(grid[r1][c1]==-1 or grid[r2][c2]==-1):
                    return -10000007
                if(r1==n and c1==n):
                    return grid[r1][c1]
                else:
                    t = grid[r1][c1]
                    if(c1!=c2):
                        t+=grid[r2][c2]
                    
                    a =  go(grid,r1,c1+1,c2+1,n)
                    b =  go(grid,r1,c1+1,c2,n)
                    c =  go(grid,r1+1,c1,c2+1,n)
                    d =  go(grid,r1+1,c1,c2,n)
                    
                    dp[(r1,c1,c2)] = t + max([a,b,c,d])
                    return dp[(r1,c1,c2)]
        
        n = len(grid)
        ans = go(grid,0,0,0,n-1)
        return ans if ans>0 else 0 
