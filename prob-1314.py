# MATRIX BLOCK SUM

def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        dic= {}
        for i in range(m):
            for j in range(n):
                l = i-k if(i-k>=0) else 0
                h = i+k if(i+k<m) else m-1
                s = j-k if(j-k>=0) else 0
                b = j+k if(j+k<n) else n-1
                if((l,h,s,b) in dic.keys()):
                    ans[i][j] = dic[(l,h,s,b)]
                    continue
                su = 0
                for t in range(l,h+1):
                    su+=sum(mat[t][s:b+1])
                dic[(l,h,s,b)]=su
                ans[i][j] = su
        return ans
