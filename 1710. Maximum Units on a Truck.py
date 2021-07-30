def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        c=0
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        
        for box in boxTypes:
            if( truckSize>=box[0] ):
                c+=(box[0]*box[1])
                truckSize-=box[0]
            else:
                c+=(truckSize*box[1])
                break
            if(truckSize==0):
                break
        
        return c
