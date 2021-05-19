def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        tup = []
        l = len(arr)
        for i in range(l-2):
            for j in range(i+1,l-1):
                if( abs(arr[i]-arr[j]) <= a ):
                    tup.append((i,j))
        
        count = 0
     
        for res in tup:
            i = res[0]
            j = res[1]
            for k in range(j+1,l):
                if( abs(arr[i]-arr[k]) <= c and abs(arr[j]-arr[k]) <= b):
                    count+=1
                
        return count
