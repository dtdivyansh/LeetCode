def numIdenticalPairs(self, nums: List[int]) -> int:
        dic =  {}
        count = 0
        for n in nums:
            if(n in dic):
                count+=dic[n]
                dic[n]+=1
            else:
                dic[n] = 1
        return count
