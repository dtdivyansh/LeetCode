def romanToInt(self, s: str) -> int:
        rep="IVXLCDM"
        num=[1,5,10,50,100,500,1000]
        val=0
        for i in range(len(s)-1):
            if(rep.index(s[i]) < rep.index(s[i+1])):
                val=val-num[rep.index(s[i])]
            else:
                val=val+num[rep.index(s[i])]
        val=val+num[rep.index(s[len(s)-1])]
        return val
