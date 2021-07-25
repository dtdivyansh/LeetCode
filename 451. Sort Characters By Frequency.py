def frequencySort(self, s: str) -> str:
        heap = []
        dic = {}
        size=0
        for i in s:
            if(i in dic.keys()):
                dic[i]+=1
            else:
                dic[i]=1
                size+=1
        
        for key,val in dic.items():
            hq.heappush(heap,(-val,key))
        
        res = ""
        while(size):
            h = hq.heappop(heap)
            res = res + (-h[0])*h[1]
            size-=1
        
        return res
