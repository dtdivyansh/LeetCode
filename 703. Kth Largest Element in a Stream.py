class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        self.size=0
        for i in nums:
            hq.heappush(self.heap,i)
            self.size+=1
            if(self.size>k):
                hq.heappop(self.heap)
                self.size-=1
        

    def add(self, val: int) -> int:
        if(self.size<self.k):
            hq.heappush(self.heap,val)
            self.size+=1
            return self.heap[0]
        
        top = self.heap[0]
        if(top>val):
            return top
        else:
            hq.heappop(self.heap)
            hq.heappush(self.heap,val)
            return self.heap[0]
