def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j,c=0,0,0
        
        while(i<len(g) and j<len(s)):
            if(s[j]>=g[i]):
                j+=1
                i+=1
                c+=1
            else:
                j+=1
        
        return c
