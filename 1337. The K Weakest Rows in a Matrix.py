def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        size = 0
        for row in range(len(mat)):
            soldier = sum(mat[row])
            if(soldier==0):
                soldier = 0.5
            hq.heappush(heap,(-soldier,-row))
            size+=1
            if(size>k):
                hq.heappop(heap)
                size-=1
        
        ans = []
        #print(heap,size)
        while(size):
            val = hq.heappop(heap)
            ans.insert(0,-val[1])
            size-=1
            
        return ans
