def freqAlphabets(self, s: str) -> str:
        alpha = '#abcdefghijklmnopqrstuvwxyz'
        num = 0
        res = ''
        i=0
        l=len(s)
        while(i<l-2):
            if(s[i+2]!='#' and num==0):
                res+=alpha[int(s[i])]

            elif(s[i]!='#'):
                num = num*10 + int(s[i])
                
            else:
                res+=alpha[num]
                num=0
            i+=1
        if(num==0):
                res+=alpha[int(s[i])]+alpha[int(s[i+1])]
        else:
            if(s[i]=='#'):
                res+=alpha[num]
                res+=alpha[int(s[i+1])]
            else:
                num = num*10 + int(s[i])
                res+=alpha[num]
                
        return res
