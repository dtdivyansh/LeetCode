def minSetSize(self, arr: List[int]) -> int:
        req = len(arr)//2
        ref = {}
        for i in arr:
            if(i in ref.keys()):
                ref[i]+=1
            else:
                ref[i]=1
                
        ans = sorted(ref.items(),key=lambda x:x[1],reverse=True)
        l=0
        for k,v in ans:
            req-=v
            l+=1
            if(req<=0):
                return l
        
 def minSetSize(self, arr: List[int]) -> int:
        heap = []
        dic = {}
        for i in arr:
            if(i in dic.keys()):
                dic[i]+=1
            else:
                dic[i]=1
        size = 0
        for key,c in dic.items():
            hq.heappush(heap,(-c,key))
            
        l = len(arr)//2
        while(l>0):
            val = hq.heappop(heap)
            l = l + val[0]
            size+=1
        
        return size
