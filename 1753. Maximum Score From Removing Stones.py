def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = []
        hq.heappush(heap,-a)
        hq.heappush(heap,-b)
        hq.heappush(heap,-c)
        c=0
        while(True):
            a = -hq.heappop(heap)
            b = -hq.heappop(heap)
            if(a==0 or b==0):
                break
            else:
                a = a-1
                b = b-1
                c+=1
                hq.heappush(heap,-a)
                hq.heappush(heap,-b)
        
        return c
