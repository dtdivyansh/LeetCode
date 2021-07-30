def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        n = len(strs[0])
        
        for i in range(n):
            p = ''
            for s in strs:
                p+=s[i]
            
            if(p!=''.join(sorted(p))):
                c+=1
        
        return c
