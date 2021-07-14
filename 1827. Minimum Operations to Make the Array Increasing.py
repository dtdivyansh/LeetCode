def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(1,len(nums)):
            if(nums[i]<=nums[i-1]):
                v = nums[i-1]-nums[i]+1
                nums[i] += v
                c += v
        return c
