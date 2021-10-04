    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e=-1
        o=0
        l = len(nums)
        while(o<l):
            if(nums[o]&1):
                pass
            else:
                e+=1
                nums[o],nums[e] = nums[e],nums[o]
            o+=1
        
        return nums
