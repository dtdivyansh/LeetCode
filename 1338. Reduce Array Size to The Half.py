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
