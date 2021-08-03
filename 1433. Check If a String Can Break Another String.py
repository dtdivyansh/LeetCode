def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a = list(map(str,s1))
        b = list(map(str,s2))
        a.sort()
        b.sort()
        if(a[0]>b[0]):
            flag=True
        elif(a[0]<b[0]):
            flag=False
        else:
            flag= -1
        
        for i in range(1,len(a)):
            if(flag==True):
                if(a[i]<b[i]):
                    return False
            elif(flag==False):
                if(a[i]>b[i]):
                    return False
            else:
                if(a[i]>b[i]):
                    flag=True
                elif(a[i]<b[i]):
                    flag=False
                    
        return True
