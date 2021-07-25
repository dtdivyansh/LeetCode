def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        size=0
        for i in stones:
            hq.heappush(heap,-i)
            size+=1
        
        while(size>1):
            y = -hq.heappop(heap)
            size-=1
            x = -hq.heappop(heap)
            size-=1
            if(x==y):
                continue
            elif(x<y):
                v = y-x
                hq.heappush(heap,-v)
                size+=1
        if(size==0):
            return 0
        else:
            return -hq.heappop(heap)
