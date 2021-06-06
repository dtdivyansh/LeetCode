def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for i in s:
            if(i=='A'):
                a+=1
                l=0
                if(a==2):
                    return False
            elif(i=='L'):
                l+=1
                if(l==3):
                    return False
            else:
                l=0
        return True
