def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True
        l = len(flowerbed)
        if(l==1 and flowerbed[0]==0):
            if(n<=1):
                return True
            else:
                return False
        if(l==1 and flowerbed[0]==1):
            if(n==0):
                return True
            else:
                return False
            
        for i in range(l):
            if(i==0):
                if(flowerbed[i]==0 and flowerbed[i+1]==0):
                    flowerbed[i]=1
                    n-=1
                
            elif(i==l-1):
                if(flowerbed[i]==0 and flowerbed[i-1]==0):
                    flowerbed[i]=1
                    n-=1
            
            else:
                if( flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0 ):
                    flowerbed[i]=1
                    n-=1
                    
            if(n==0):
                return True
        return False
