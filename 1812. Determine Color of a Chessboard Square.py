def squareIsWhite(self, coordinates: str) -> bool:
        dic = {'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5 , 'f':6 , 'g':7 , 'h':8}
        c=1
            
        d = dic[ coordinates[0] ]
        u = int(coordinates[1])
        
        if((u-d)%2==0):
            return False
        else:
            return True
