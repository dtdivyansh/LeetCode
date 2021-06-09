def balancedStringSplit(self, s: str) -> int:
        c = 0
        R = 0
        for i in s:
            if( i =='R' ):
                R+=1
            else:
                R-=1
            if( not R ):
                c+=1
        return c
