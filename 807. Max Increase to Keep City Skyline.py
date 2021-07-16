def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        new = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            maxi = max(grid[i])
            for j in range(m):
                new[i][j]=maxi
                
        for j in range(m):
            maxi = max([grid[i][j] for i in range(n)])
            
            for i in range(n):
                new[i][j] = min( new[i][j],maxi )
                
        c = 0
        for i in range(n):
            for j in range(m):
                v = new[i][j] - grid[i][j]
                c+=v
        
        return c
