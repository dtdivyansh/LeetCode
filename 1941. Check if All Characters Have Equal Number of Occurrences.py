def areOccurrencesEqual(self, s: str) -> bool:
        ans = False
        dic = {}
        m=-1
        for i in s:
            if(i in dic ):
                dic[i]+=1
                
            else:
                dic[i]=1
        
        for i in dic.values():
            if(m<0):
                m=i
            if(i!=m):
                return False
        
        return True
