def minSteps(self, s: str, t: str) -> int:
        count = 0
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        dic1 = {}
        dic2 = {}
        for val in alpha:
            dic2[val] = t.count(val)
            dic1[val] = s.count(val)
            
        for i in dic2:
            c1 = dic2[i]
            c2 = dic1[i]
            if(c1>c2):
                count+=(c1-c2)
                
        return count
