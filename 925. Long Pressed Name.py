def isLongPressedName(self, name: str, typed: str) -> bool:
        flag = True
        i,j=0,0
        n,m=len(name),len(typed)
        if(n>m):
            return False
        while(i<n and j<m):
            c=1
            if(i<n-1):
                while(name[i]==name[i+1]):
                    i+=1
                    c+=1
                    if(i==n-1):
                        break
            k=0
            while(name[i]==typed[j]):
                j+=1
                k+=1
                if(j>=m):
                    j-=1
                    break
            if(c>k):
                return False
            if(i==n-1 and name[i]!=typed[j]):
                return False
    
            i+=1
        
        return True
