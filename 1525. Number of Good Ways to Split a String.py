def numSplits(self, s: str) -> int:
        a,b = [],[]
        dic = {}
        c=0
        for i in s:
            if(i not in dic.keys()):
                c+=1
                dic[i] = 1
                a.append(c)
            else:
                a.append(c)
        c=0
        dic = {}
        for i in s[::-1]:
            if(i not in dic.keys()):
                c+=1
                dic[i] = 1
                b.insert(0,c)
            else:
                b.insert(0,c)
        c=0
        for i in range(len(s)-1):
            if(a[i]==b[i+1]):
                c+=1
            if(a[i]>b[i]):
                break
        
        return c
