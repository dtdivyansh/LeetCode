# Minimum falling path sum

def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = {}
        def minPath(matrix,r,c):
            if((r,c) in dp.keys()):
                return dp[(r,c)]
            if(r>=len(matrix)-1):
                dp[(r,c)] = matrix[r][c]
                return matrix[r][c]
            else:
                p,q,s=1000,1000,1000
                if(c-1>=0):
                    p = minPath(matrix,r+1,c-1)
                if(c+1<len(matrix[0])):
                    q = minPath(matrix,r+1,c+1)
                s = minPath(matrix,r+1,c)
                dp[(r,c)] = matrix[r][c] + min(p,q,s)
                return dp[(r,c)]
            
        mini = float('inf')
        for c1 in range(len(matrix[0])):
            v = minPath(matrix,0,c1)
            mini = min(v,mini)
        return mini
