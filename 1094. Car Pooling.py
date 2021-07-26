def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        head,tail = 1001,0
        start = {}
        end = {}
        for trip in trips:
            if(trip[1] in start.keys() ):
                start[trip[1]]+=trip[0]
            else:
                start[trip[1]] = trip[0]
            head = min(head,trip[1])
            
            if(trip[2] in end.keys() ):
                end[trip[2]]+=trip[0]
            else:
                end[trip[2]] = trip[0]
            tail = max(tail,trip[2])
            
        
        c = 0
        for i in range(head,tail+1):
            if( i in end.keys() ):
                c-=end[i]
                
            if(i in start.keys()):
                c+=start[i]
                
            if(c>capacity):
                return False
            
        return True
