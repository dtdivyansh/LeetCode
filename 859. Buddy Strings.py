def buddyStrings(self, s: str, goal: str) -> bool:
        a = len(s)
        b = len(goal)
        if(a!=b):
            return False
        else:
            c,d=0,0
            dic = {}
            for i in range(a):
                if(s[i]!=goal[i]):
                    c+=1
                    dic[c] = (s[i],goal[i])
                else:
                    if(s[i] in dic.keys()):
                        d=2
                    dic[s[i]]=1
                    
                if(c>2):
                    return False
                
            if(c==2):
                if( dic[1][0]==dic[2][1] and dic[1][1]==dic[2][0] ):
                    return True
                else:
                    return False        
                
            if(c==0 and d==2):
                return True
            else:
                return False
