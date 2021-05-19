def shuffle(self, nums: List[int], n: int) -> List[int]:
        if(not nums):
            return nums
        mid = n
        start = 0
        while(start!=2*n-2):
            val = nums.pop(mid)
            nums.insert(start+1,val)
            start+=2
            mid+=1
        return nums
        
