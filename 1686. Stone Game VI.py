def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        heap = []
        for i in range(n):
            s = aliceValues[i] + bobValues[i]
            hq.heappush(heap,( -s, [aliceValues[i],bobValues[i]] ))
        
        a,b = 0,0
        for i in range(n):
            h = hq.heappop(heap)
            if(i&1):
                b+=h[1][1]
            else:
                a+=h[1][0]
        if(a==b):
            return 0
        elif(a>b):
            return 1
        else:
            return -1
