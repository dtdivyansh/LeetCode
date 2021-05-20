def countSort(self,l):
        arr = [0]*101
        for i in l:
            arr[i]+=1
            
        sortedArr = []
        for i in range(len(arr)):
            for j in range(1,arr[i]+1):
                sortedArr.append(i)
                
        return sortedArr
    
    def sorting(self,mat,col,row,c,r):
        l = []
        r1=r
        c1=c
        while(r<row and c<col): # inserting diagnol elements in a list
            l.append(mat[r][c])
            r+=1
            c+=1
        
        #l = self.countSort(l)  Turned out to be slower
        l.sort()
        
        while(r1<row and c1<col):  # inserting sorted elements in matrix diagonally
            mat[r1][c1] = l.pop(0)
            r1+=1
            c1+=1
        
    
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        for i in range(col-1):  # sorting column wise hence r=0
            self.sorting(mat,col,row,i,0)
            
        for i in range(1,row-1): # sorting row wise hence c=0
            self.sorting(mat,col,row,0,i)  
        
        return mat
