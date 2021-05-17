# Count Square Submatrix with all one's

def countSquares(self, matrix: List[List[int]]) -> int:
        c = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                if(num==0):
                    dp[i][j]=0
                else:
                    if(i==0 or j==0):
                        dp[i][j] = num
                        c+=dp[i][j]
                    else:
                        mini = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                        dp[i][j] = 1 + mini
                        c+=dp[i][j]
        return c
        
