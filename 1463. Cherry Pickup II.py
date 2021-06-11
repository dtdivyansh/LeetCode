 def cherryPickup(self, grid: List[List[int]]) -> int:
        def solve(grid,c1,c2,r,row,col):
            if(c1<0 or c2<0 or c1>col or c2>col or r>row):
                return 0
            
            if((c1,c2,r) in dic.keys()):
                return dic[(c1,c2,r)]
            
            else:
                total = grid[r][c1]
                
                if(c1!=c2):
                    total = total+grid[r][c2]
                 
                a = total+solve(grid,c1,c2,r+1,row,col)
                b = total+solve(grid,c1,c2+1,r+1,row,col)
                d = total+solve(grid,c1,c2-1,r+1,row,col)
                
                a1 = total+solve(grid,c1+1,c2,r+1,row,col)
                b1 = total+solve(grid,c1+1,c2+1,r+1,row,col)
                d1 = total+solve(grid,c1+1,c2-1,r+1,row,col)
                
                a2 = total+solve(grid,c1-1,c2,r+1,row,col)
                b2 = total+solve(grid,c1-1,c2+1,r+1,row,col)
                d2 = total+solve(grid,c1-1,c2-1,r+1,row,col)
                
                m = max([a,b,d,a1,b1,d1,a2,b2,d2])
                dic[(c1,c2,r)] = m 
                return m
            
        col = len(grid[0])
        row = len(grid)
        dic = {}
        ans1 = solve(grid,0,col-1,0,row-1,col-1)

        return ans1
