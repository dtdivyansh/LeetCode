def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in range(1,len(nums)):
            dic[i]=True
            
        for i in nums:
            if(dic[i]):
                dic[i]=False
            else:
                return i
