def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        
        def fun(link):
            nonlocal dic
            link = link.split()
            c = int(link[0])
            s = link[1]
            
            if(s not in dic):
                dic[s] = c
            else:
                dic[s]+=c
                
            while('.' in s):
                i = s.index('.')
                s = s[i+1:]
                if(s not in dic):
                    dic[s] = c
                else:
                    dic[s]+=c
                    
        for l in cpdomains:
            fun(l)
            
        ans = []
        
        for key,val in dic.items():
            a = str(val)+' '+key
            ans.append(a)
            
        return ans
