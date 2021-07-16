def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        ans = 0
        while(i<j):
            s = nums[i]+nums[j]
            ans = max(s,ans)
            i+=1
            j-=1
        return ans
