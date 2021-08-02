def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            if(i in dic.keys()):
                dic[i]+=1
            else:
                dic[i]=1
        
        val = list(dic.values())
        c=0
        v=0
        for i in val:
            if(i&1):
                c+=(i-1)
                if(v==0):
                    c+=1
                    v=1
            else:
                c+=i
        return c
