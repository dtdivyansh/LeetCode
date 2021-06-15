def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        '''
        arr = [0 for i in range(n)]
        for i in range(n):
            if(nums[i]<n and arr[nums[i]]==0):
                arr[nums[i]]=1
            elif(nums[i]<n):
                ans.append(nums[i])
        '''
        dic = {}
        for i in range(n):
            if(nums[i] in dic.keys()):
                ans.append(nums[i])
            else:
                dic[nums[i]]=1
        return ans
