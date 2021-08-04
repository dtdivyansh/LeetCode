def maximumTime(self, time: str) -> str:
        time = time.split(':')
        h,m = time[0],time[1]
        res=''
        
        if(h[0]=='?'):
            if(h[1]=='?' or h[1] in '0123'):
                res+='2'
            else:
                res+='1'
        else:
            res+=h[0]
            
        if(h[1]=='?'):
            if(res[-1]=='2'):
                res+='3'
            else:
                res+='9'
        else:
            res+=h[1]
        res+=':'
            
        if(m[0]=='?'):
            res+='5'
        else:
            res+=m[0]
            
        if(m[1]=='?'):
            res+='9'
        else:
            res+=m[1]
            
        return res
