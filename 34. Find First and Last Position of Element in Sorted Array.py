def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first(nums,target,start,end):
            fi = 10**5
            while(start<=end):
                mid = (start+end)//2
                if(nums[mid]==target):
                    fi = mid
                    end = mid-1
                elif(nums[mid]<target):
                    start = mid+1
                else:
                    end = mid-1
            return fi
        
        def last(nums,target,start,end):
            la = -1
            while(start<=end):
                mid = (start+end)//2
                if(nums[mid]==target):
                    la = mid
                    start = mid+1
                elif(nums[mid]<target):
                    start = mid+1
                else:
                    end = mid-1
            return la
        
        start,end = 0,len(nums)-1
        f = first(nums,target,start,end)
        l = last(nums,target,start,end)
        if(l==-1):
            return [-1,-1]
        return [f,l]
