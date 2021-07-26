def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        size=0
        for i in nums:
            hq.heappush(heap,i)
            size+=1
        
        arr = []
        while(size>0):
            val = hq.heappop(heap)
            arr.append(val)
            size-=1
        
        return arr
