#https://leetcode.com/problems/maximize-sum-of-array-after-k-negations

def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        n=len(nums)
        while(k and i<n):
            if(nums[i]==0):
                break
            else:
                if(nums[i]<0):
                    if(i<n-1 and nums[i+1]>=0):
                        if(k&1):
                            nums[i] = -nums[i]
                            break
                        else:
                            nums[i] = -nums[i]
                            k = 1
                            i+=1
                            if(nums[i]>nums[i-1]):
                                nums[i-1] = -nums[i-1]
                                break
                    else:
                        nums[i] = -nums[i]
                        k-=1
                        i+=1
                else:
                    if(k&1):
                        nums[i] = -nums[i]
                        break
                    else:
                        break
                    
        return sum(nums)
