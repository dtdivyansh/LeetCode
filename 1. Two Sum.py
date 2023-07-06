#https://leetcode.com/problems/two-sum

# NAIVE APPROACH

def twoSum(self, nums, target):
        k=len(nums)
        for i in range(k):
            for j in range(i+1,k):
                if(nums[i]+nums[j]==target):
                    return [i,j]

        
# OPTIMIZED APPROACH

def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ans = []
        for i in range(len(nums)):
            if(target-nums[i] in dic.keys()):
                ans = [i,dic[target-nums[i]]]
                break
            if(nums[i] not in dic.keys()):
                dic[nums[i]]=i
                
        return ans
