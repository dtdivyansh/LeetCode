def countSegments(self, s: str) -> int:
        seg=0
        flag=1
        for i in  s:
            if(i!=" " and flag==1):
                flag=0
                seg+=1
            if(i==" "):
                flag=1
        return seg
