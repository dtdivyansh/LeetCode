def countKDifference(self, nums: List[int], k: int) -> int:
        dic = {}
        for i in nums:
            if(i not in dic ):
                dic[i]=1
            else:
                dic[i]+=1
        
        c=0
        for i in nums:
            if( i+k in dic):
                c+=dic[i+k]
        
        return c
