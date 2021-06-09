def modifyString(self, s: str) -> str:
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alpha = [i for i in alpha]
        res = '.'
        for i in range(len(s)):
            if(s[i]!='?'):
                res+=s[i]
            else:
                k1 = res[-1]
                if(i==len(s)-1):
                    k2 = '.'
                else:
                    k2 = s[i+1]
                for j in alpha:
                    if(j!=k1 and j!=k2):
                        res+=j
                        break
            
        return res[1:]
