def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        n = len(nums)
        for i in nums:
            if(i&1):
                odd.append(i)
            else:
                even.append(i)
        
        for i in range(n):
            if(i&1):
                nums[i] = odd.pop()
            else:
                nums[i] = even.pop()
        
        return nums
