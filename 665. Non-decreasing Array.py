def checkPossibility(self, nums: List[int]) -> bool:
        c=0
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                if(c):
                    return False
                else:
                    if(i==1):
                        nums[i-1] = nums[i]
                        c+=1
                    else:
                        if(nums[i-2]<=nums[i]):
                            nums[i-1] = nums[i-2]
                            c+=1
                        else:
                            nums[i] = nums[i-1]
                            c+=1
        return True
