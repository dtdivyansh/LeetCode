def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = []
        for i in range(n):
            val = [i*0 for i in range(m)]
            mat.append(val)
            
        for ri,ci in indices:
            for i in range(m):
                mat[ri][i]+=1
            for j in range(n):
                mat[j][ci]+=1
                
        from functools import reduce    
        c = 0
        
        for i in reduce(lambda x,y: x+y,mat):
            if(i&1==1):
                c+=1
        return c
