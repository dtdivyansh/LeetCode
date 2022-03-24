def countPoints(self, rings: str) -> int:
        dic={}
        for i in range(10):
            dic[i] = {'R':0, 'G':0, 'B':0}
            
        c=0
        for i in range(0,len(rings)-1,2):
            dic[int(rings[i+1])][rings[i]]=1
            
        for dep in dic.values():
            if(dep['R']+dep['G']+dep['B']==3):
                c+=1
        
        return c
