def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        row = [10**5+1 for i in range(m)]
        col = [0 for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                row[i] = min(row[i],matrix[i][j])
                col[j] = max(col[j],matrix[i][j])
        
        ans = []
        
        for i in range(m):
            for j in range(n):
                if(row[i]==col[j]):
                    ans.append(row[i])
        
        return ans
