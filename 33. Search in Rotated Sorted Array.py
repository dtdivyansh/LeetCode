def search(self, nums: List[int], target: int) -> int:
        
        def mini(nums):
            i,j=0,len(nums)-1
            v,m=1000007,-1
            while(i<=j):
                mid = (i+j)//2
                if(nums[mid]<v):
                    v=nums[mid]
                    m=mid
                if(nums[mid]>=nums[0] and nums[mid]<=nums[-1]):
                    return 0
                elif(nums[mid]>=nums[0]):
                    i = mid+1
                else:
                    j=mid-1
            return m
        
        mi = mini(nums)
    
        if(mi==len(nums)-1 and nums[mi]==target):
            return mi
        if(target<nums[0] or mi==0):
            i=mi
            j=len(nums)-1
        else:
            i=0
            j=mi-1
        
        while(i<=j):
            mid = (i+j)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                i = mid+1
            else:
                j=mid-1
        return -1
