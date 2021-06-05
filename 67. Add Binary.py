def addBinary(self, a: str, b: str) -> str:
        l=""
        m=""
        if(len(a)>len(b)):
            l=b
            m=a
        else:
            l=a
            m=b
        l="0"*(len(m)-len(l))+l
        res=""
        carry=0
        for i in range(len(m)-1,-1,-1):
            c= int(l[i]) + int(m[i]) + carry
            if(c>1):
                carry=1
            else:
                carry=0
            res=str(c%2)+res
        if(carry==1):
            res="1"+res
        return res
