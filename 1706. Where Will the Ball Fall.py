def findBall(self, grid: List[List[int]]) -> List[int]:
    
        def solve(grid,c,r,col,row):
            if(dp[r][c]!=-2):
                return dp[r][c]
            if(r>row):
                return c
            if(c<0 or c>col):
                return -1
            
            if(c==0 and grid[r][c]==-1): #left corner
                dp[r][c]=-1
                return -1
            
            if(c==col and grid[r][c]==1): # right corner
                dp[r][c]=-1
                return -1
            
            if( (c<col and grid[r][c]==1 and grid[r][c+1]==-1) or (c>0 and grid[r][c]==-1 and grid[r][c-1]==1) ):#V-shape
                dp[r][c]=-1
                return -1
            
            else:
                if(grid[r][c]==-1):
                    dp[r][c]= solve(grid,c-1,r+1,col,row)
                else:
                    dp[r][c]= solve(grid,c+1,r+1,col,row)
                    
                return dp[r][c]
                
        col = len(grid[0])
        row = len(grid)
        ans = [0 for i in range(col)]
        dp = [[-2 for i in range(col+1)] for j in range(row+1) ]
        for i in range(col):
            ans[i] = solve(grid,i,0,col-1,row-1)
            
        return ans
