def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        nums.sort()
        l = len(nums)
        if(l==1):
            return nums
        
        ans = []
        new = 0
        while(new<=s-new):
            l-=1
            ans.append(nums[l])
            new+=nums[l]
            
        return ans
