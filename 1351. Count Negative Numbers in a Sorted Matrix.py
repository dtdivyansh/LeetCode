def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        i,j=0,0
        c=0
        while(i<m):
            while(j<n):
                if(grid[i][j]<0):
                    c+=(n-j)*(m-i)
                    n = j
                    break
                else:
                    j+=1
            j=0
            i+=1
        
        return c
