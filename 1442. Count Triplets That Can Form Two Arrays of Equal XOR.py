def countTriplets(self, arr: List[int]) -> int:
        l = len(arr)
        if(l==1):
            return 0
        if(l==2):
            if(arr[0]==arr[1]):
                return 1
            else:
                return 0
            
        i,j,k=0,1,1
        new = [0 for i in range(l+1)]
        for i in range(1,l+1):
            new[i] = new[i-1]^arr[i-1]
        c=0
        """
        for i in range(1,l+1):
            for j in range(i+1,l+1):
                for k in range(j,l+1):
                    if(new[j-1]^new[i-1]==new[k]^new[j-1]):
                        c+=1
        """
        for i in range(1,l+1):
            for k in range(i+1,l+1):
                if(new[k]^new[i-1]==0):
                    c = c + k-i
                
        return c
