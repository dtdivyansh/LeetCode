def proceed(self,nums ,rows ,final ):
        if(rows>final):
            return nums
        rn=ceil(rows/2)
        ls=[1]
        i=1
        while(i<rn):
            ls.append(nums[-1][i-1]+nums[-1][i])
            i+=1
        if(rows%2==0):
            i-=1
        else:
            i-=2
        while(i>0):
            ls.append(ls[i])
            i-=1
        ls.append(1)
        nums.append(ls)
        return self.proceed(nums,rows+1,final)
            
        
        
        
    
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1],[1,1]]
        if(numRows==0):
            return []
        if(numRows==1):
            return [[1]]
        if(numRows==2):
            return l
        return self.proceed(l,3,numRows)
