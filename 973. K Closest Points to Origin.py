import heapq as hq
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        p=k
        for co in points:
            x = co[0]
            y = co[1]
            dist = (x**2 + y**2)**(0.5)
            hq.heappush(heap,(-dist,[x,y]))
            k-=1
            if(k<0):
                hq.heappop(heap)
                k+=1
        
        ans = []
        while(k<p):
            v = hq.heappop(heap)
            ans.append(v[1])
            k+=1
        return ans
